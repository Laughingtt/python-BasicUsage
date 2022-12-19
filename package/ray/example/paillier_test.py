import ray
import time
from phe import paillier

ray.init(address="10.10.10.241:9937")


class Test:

    def gen_pubk(self):
        pubk, prik = paillier.generate_paillier_keypair(n_length=1024)

        return pubk, prik

    @staticmethod
    @ray.remote
    def encrypt(pubk, num):
        return pubk.encrypt(num)

    @staticmethod
    @ray.remote
    def encrypt_batch(pubk, num):
        lis = []
        for i in range(num):
            lis.append(pubk.encrypt(i))
        return lis


class Run(object):
    def encrypt_test(self):
        t = Test()
        pubk, prik = t.gen_pubk()
        task = []
        t0 = time.time()
        for i in range(10000):
            task.append(t.encrypt.remote(pubk=pubk, num=i))
        ray.get(task)

        print("encrypt_test func time is {}".format(time.time() - t0))

        # 9s

    def encrypt_batch(self):
        t = Test()
        pubk, prik = t.gen_pubk()
        t0 = time.time()
        task = []
        for i in range(20):
            task.append(t.encrypt_batch.remote(pubk=pubk, num=500))
        ray.get(task)

        print("encrypt_test func time is {}".format(time.time() - t0))

        # 8.3s

    def encrypt_single_thread(self):
        t = Test()
        pubk, prik = t.gen_pubk()
        task = []
        t0 = time.time()
        for i in range(1000):
            task.append(pubk.encrypt(i))

        print("encrypt_test func time is {}".format(time.time() - t0))

        # 160s


if __name__ == '__main__':
    r = Run()
    r.encrypt_test()
    r.encrypt_single_thread()
