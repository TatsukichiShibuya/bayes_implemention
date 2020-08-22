import numpy as np
import matplotlib.pyplot as plt


def show(x, title):
    plt.hist(x, bins=50, range=(-10, 10))
    plt.title(title)
    plt.show()


def p_childa(z):
    ave = 3
    std = 2
    return np.exp(-(z - ave)**2 / std**2)


def dp_childa(z):
    ave = 3
    std = 2
    return -(z - ave) / std**2 * p_childa(z)


def accept(r):
    u = np.random.rand()
    return (r >= u)


def RejectionSampling(num):
    def q_sample():  # Uni(-10,10)
        return (np.random.rand() - 0.5) * 20

    def q(z):
        return 1 / 20
    k = 20
    sample = np.zeros(0)
    for i in range(num):
        z = q_sample()
        u = np.random.rand() * k * q(z)
        if u <= p_childa(z):
            sample = np.append(sample, z)
    show(sample, "RejectionSamplng")


def MetropolisHastings(num):
    def q_sample(z_):
        return np.random.normal(z_, 1)

    def q(z, z_):
        return np.exp(-(z - z_)**2 / 2) / np.sqrt(2 * np.pi)
    z = 1
    sample = np.zeros(0)
    for i in range(num):
        z_ = q_sample(z)
        r = (p_childa(z_) * q(z, z_)) / (p_childa(z) * q(z_, z))
        if accept(min(1, r)):
            z = z_
            sample = np.append(sample, z)
    show(sample, "MetropolisHastings")


def HMC(num):
    def p_sample():
        return np.random.normal(0, 1)
    z = 1
    sample = np.zeros(0)
    for i in range(num):
        p = p_sample()
        p1_2 = p + dp_childa(z) / p_childa(z) / 2
        z_ = z + p1_2
        p_ = p1_2 + dp_childa(z) / p_childa(z) / 2
        r = np.exp(np.log(p_childa(z_)) - p_**2 / 2) / np.exp(np.log(p_childa(z)) - p**2 / 2)
        if accept(min(1, r)):
            z = z_
            sample = np.append(sample, z)
    show(sample, "HMC")


def main(num=1000):
    RejectionSampling(num)
    MetropolisHastings(num)
    HMC(num)


if __name__ == '__main__':
    main()
