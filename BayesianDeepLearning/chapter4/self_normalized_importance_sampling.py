import numpy as np


def f(z):
    return z


def p_(z):
    prob = [3, 4, 7, 8, 2, 1]
    return prob[z - 1]


def q_(z):
    prob = [1, 1, 1, 1, 1, 1]
    return prob[z - 1]


a = b = 0
for i in range(1000):
    z = np.random.randint(1, 7)
    a += f(z) * p_(z) / q_(z)
    b += p_(z) / q_(z)
print("E[f(z)]=" + str(a / b))  # f(z)=zの時、3.2が理論値
