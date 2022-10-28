#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 提取工厂类

"""
Todays refactoring was first coined by the GangOfFour and has many resources on the web that have different usages of this pattern. 
Two different aims of the factory pattern can be found on the GoF website here and here.

Often in code some involved setup of objects is required in order to get them into a state where we can begin working with them. 
Uusally this setup is nothing more than creating a new instance of the object and working with it in whatever manner we need. 
Sometimes however the creation requirements of this object may grow and clouds the original code that was used to create the object. 
This is where a Factory class comes into play. For a full description of the factory pattern you can read more here. 
On the complex end of the factory pattern is for creating families of objects using Abstract Factory. 
Our usage is on the basic end where we have one factory class creating one specific instance for us. 
Take a look at the code before:
"""
# 今天的重构是由 GangOfFour 首先提出的，网络上有很多关于该模式不同用法的资源。
# 在 GoF 网站上的这里 和这里有关于工厂模式的两个不同用法。
# 在代码中，通常需要一些复杂的对象创建工作，以使这些对象达到一种可以使用的状态。
# 通常情况下，这种创建不过是新建对象实例，并以我们需要的方式进行工作。
# 但是，有时候这种创建对象的需求会极具增长，并且混淆了创建对象的原始代码。
# 这时，工厂类就派上用场了。
# 关于工厂模式更全面的描述可以参考这里。
# 最复杂的工厂模式是使用抽象工厂创建对象族。
# 而我们只是使用最基本的方式，用一个工厂类创建一个特殊类的实例。
# 来看下面的代码:

from abc import ABCMeta, abstractmethod


class PoliceCar: pass


class PolliceCarController:
    def new_car(self, mileague, service_required):
        policecar = PoliceCar()
        policecar.service_required = service_required
        policecar.mileague = mileague
        return policecar


"""
As we can see, the new action is responsible for creating a PoliceCar and then setting some initial properties 
on the police car depending on some external input. 
This works fine for simple setup, but over time this can grow and the burden of creating the police car 
is put on the controller which isn’t really something that the controller should be tasked with. 
In this instance we can extract our creation code and place in a Factory class 
that has the distinct responsibility of create instances of PoliceCar’s
"""


# 如您所见，new_car 方法负责创建 PoliceCar 并根据一些外部输入初始化 PoliceCar 的某些属性。
# 对于简单的创建工作来说，这样做可以从容应对。
# 但是久而久之，创建的工作量越来越大，并且被附加在 controller 类上， 但这并不是 controller 类的职责。
# 这时，我们可以将创建代码提取到一个 Factory 类中去，由该类负责 PoliceCar 实例的创建。

class PoliceCar: pass


class IPoliceCarFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self, mileague, service_required): raise NotImplementedError()


class PoliceCarFactory(IPoliceCarFactory):
    def create(self, mileague, service_required):
        policecar = PoliceCar()
        policecar.service_required = service_required
        policecar.mileague = mileague
        return policecar


class PolliceCarController:
    def __init__(self, i_policecar_factory):
        self.i_policecar_factory = i_policecar_factory

    def new_car(self, mileague, service_required):
        return self.i_policecar_factory.create(mileague, service_required)


"""
Now that we have the creation logic put off to a factory, 
we can add to that one class that is tasked with creating instances for us without the worry of missing something 
during setup or duplicating code.
"""

# 由于将创建的逻辑转移到了工厂中，我们可以添加一个类来专门负责实例的创建，而不必担心在创建或复制代码的过程中有所遗漏。
