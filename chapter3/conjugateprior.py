import copy
import argparse
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt
import random


class Beta:
    def __init__(self, hparam):
        self.a = hparam[0]
        self.b = hparam[1]
        self.mu = 0.4  # 生成されるデータ値の真の平均

    def update(self, num=1):
        for i in range(num):
            x = random.random()
            if x < self.mu:
                self.a += 1
            else:
                self.b += 1
        return self

    def show(self):
        x = np.linspace(0, 1, num=1000)
        plt.plot(x, beta.pdf(x, self.a, self.b),
                 label='a={},b={},n={}'.format(self.a, self.b, self.a+self.b))
        plt.legend()
        plt.show()


class Distribution:
    def __init__(self, name, hparam):
        self.distribution = name

        if(self.distribution == 'beta'):
            self.model = Beta(hparam)
        else:
            pass

    def updata(self, num=1):
        self.model.update(num)
        return self

    def show(self):
        self.model.show()


def main(**kwargs):  # 流れの再現を重視しているため、多少非効率な実装になっている
    num = kwargs['updatetimes']
    size = kwargs['updatesize']
    cprior = Distribution(name=kwargs['model'], hparam=kwargs['hyperparam'])
    for i in range(num):
        posterior = copy.deepcopy(cprior.updata(num=size))  # 更新
        if num <= 10 or i % (num//10) == 0:  # 分布の表示
            posterior.show()
        cprior = posterior  # 事後分布を事前分布に当てはめる
    posterior.show()
    del posterior


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument(
        '-m', '--model', type=str, required=True
    )
    parser.add_argument(
        '-t', '--updatetimes', type=int
    )
    parser.add_argument(
        '-s', '--updatesize', type=int
    )
    parser.add_argument(
        '-p', '--hyperparam', nargs='+', type=int,
        help="例 beta:-m beta -t 100 -s 1 -p 1 1"
    )
    FLAGS = vars(parser.parse_args())
    main(**FLAGS)
