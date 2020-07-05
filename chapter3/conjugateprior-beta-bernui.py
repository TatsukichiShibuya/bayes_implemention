import copy
import argparse

class Beta:
    def __init__(self):
        self.model = 1
        self.a = 1
    def update(self, num=1):
        pass
    def show(self):
        pass

class Distribution:
    def __init__(self, name, hparam):
        self.distribution = name
        self.hparam = hparam
        if(self.distribution == "beta"):
            self.model = Beta()
        else:
            pass
    def updata(self, num=1):  # ランダムデータnum個で更新
        self.model.update(num)
        return self
    def show(self):
        self.model.show()
        
def main(**kwargs):
    num = kwargs['updatetimes']
    size = kwargs['updatesize']
    cprior = Distribution(name=kwargs['model'], hparam=kwargs['hyperparam'])
    for i in range(num):
        posterior = copy.deepcopy(cprior.updata(num=size))  # 更新
        del cprior
        print(posterior.model.a)
        if i <= 10 or i%(num//10) == 0:
            posterior.show()
            print()
        cprior = posterior
    posterior.show()
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
