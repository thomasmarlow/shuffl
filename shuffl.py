from time import time


class Shuffl:
    # TODO: force seed to be a natural number
    def __init__(self, seed):
        self.__seed=seed
        self.__miniseed=seed

    def rand(self):
        while self.__miniseed == 0:
            self.__miniseed=Shuffl(self.__seed).rand()*1000
        r=time()/(self.__miniseed*10e6)%1000000
        for _ in range(100):
            r=r**(5/2)%1000000
        self.__miniseed=r/999999
        return self.__miniseed if self.__miniseed == 0.0 else self.__miniseed-10e-17

    def choose(self, values, amount=1):
        if amount <= 0:
            raise Exception('Amount to choose must be greater than 0')
        if amount > len(values):
            raise Exception("Amount to choose can't be greater than list size")
        chosen=[]
        values_copy=values[:]
        while len(chosen) < amount:
            chosen.append(values_copy.pop(int(self.rand()*len(values_copy))))
        return chosen if len(chosen) > 1 else chosen[0]
