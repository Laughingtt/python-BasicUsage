#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/12/27 9:43 AM 
# ide： PyCharm

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
import secretflow as sf
import jax.numpy as jnp
import matplotlib.pyplot as plt


def breast_cancer(party_id=None, train: bool = True) -> (np.ndarray, np.ndarray):
    scaler = Normalizer(norm='max')
    x, y = load_breast_cancer(return_X_y=True)
    x = scaler.fit_transform(x)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    if train:
        if party_id:
            if party_id == 1:
                return x_train[:, 15:], None
            else:
                return x_train[:, :15], y_train
        else:
            return x_train, y_train
    else:
        return x_test, y_test


# In case you have a running secretflow runtime already.
sf.shutdown()

sf.init(['alice', 'bob'], num_cpus=8, log_to_driver=True)

alice, bob = sf.PYU('alice'), sf.PYU('bob')
spu = sf.SPU(sf.utils.testing.cluster_def(['alice', 'bob']))

x1, _ = alice(breast_cancer)(party_id=1)
x2, y = bob(breast_cancer)(party_id=2)

device = spu

W = jnp.zeros((30,))
b = 0.0

W_, b_, x1_, x2_, y_ = (
    sf.to(device, W),
    sf.to(device, b),
    x1.to(device),
    x2.to(device),
    y.to(device),
)

from jax import value_and_grad


def sigmoid(x):
    return 1 / (1 + jnp.exp(-x))


# Outputs probability of a label being true.
def predict(W, b, inputs):
    return sigmoid(jnp.dot(inputs, W) + b)


# Training loss is the negative log-likelihood of the training examples.
def loss(W, b, inputs, targets):
    preds = predict(W, b, inputs)
    label_probs = preds * targets + (1 - preds) * (1 - targets)
    return -jnp.mean(jnp.log(label_probs))


def train_step(W, b, x1, x2, y, learning_rate):
    x = jnp.concatenate([x1, x2], axis=1)
    loss_value, Wb_grad = value_and_grad(loss, (0, 1))(W, b, x, y)
    W -= learning_rate * Wb_grad[0]
    b -= learning_rate * Wb_grad[1]
    return loss_value, W, b


def fit(W, b, x1, x2, y, epochs=1, learning_rate=1e-2):
    losses = jnp.array([])
    for _ in range(epochs):
        l, W, b = train_step(W, b, x1, x2, y, learning_rate=learning_rate)
        losses = jnp.append(losses, l)
    return losses, W, b


def plot_losses(losses):
    plt.plot(np.arange(len(losses)), losses)
    plt.xlabel('epoch')
    plt.ylabel('loss')


from sklearn.metrics import roc_auc_score


def validate_model(W, b, X_test, y_test):
    y_pred = predict(W, b, X_test)
    return roc_auc_score(y_test, y_pred)


losses, W_, b_ = device(
    fit,
    static_argnames=['epochs'],
    num_returns_policy=sf.device.SPUCompilerNumReturnsPolicy.FROM_USER,
    user_specified_num_returns=3,
)(W_, b_, x1_, x2_, y_, epochs=10, learning_rate=1e-2)

losses = sf.reveal(losses)

plot_losses(losses)

X_test, y_test = breast_cancer(train=False)
auc = validate_model(sf.reveal(W_), sf.reveal(b_), X_test, y_test)
print(f'auc={auc}')
plt.show()
