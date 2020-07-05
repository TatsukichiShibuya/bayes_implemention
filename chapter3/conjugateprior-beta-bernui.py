import copy
import argparse

class beta():
    def __init__(self):
        self.model = 1
    def update(self):
        pass

class ConjugatePrior:
    def __init__(self, name, hparam):
        self.distributionType = name
        self.hparam = hparam
        self.model = beta()
    def updata(self, num=1):  # ランダムデータnum個で更新
        return self

def main(**kwargs):
    num = kwargs['updatetimes']
    size = kwargs['updatesize']
    cprior = ConjugatePrior(name=kwargs['model'], hparam=kwargs['hyperparam'])
    for i in range(num):
        posterior = copy.deepcopy(cprior.updata(num=size))  # 更新
        del cprior
        if i <= 10 or i%(num//10) == 0:
            # 事後分布の表示
            print(i)
    # 事後分布の表示
    del posterior

if(__name__ == "__main__"):
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
        '-p', '--hyperparam', nargs='+'
    )
    FLAGS = vars(parser.parse_args())
    main(**FLAGS)
