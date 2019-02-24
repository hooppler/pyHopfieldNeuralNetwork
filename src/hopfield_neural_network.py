"""
Copyright 2019, Aleksandar Stojimirovic <stojimirovic@yahoo.com>

Licence: MIT
Source: https://github.com/hooppler/pyHopfieldNeuralNetwork
"""

import random


class HopfieldNeuralNetwork(object):
    def __init__(self, N=None):
        
        if N == None:
            self.N = 10
            self.y = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
            self.x = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
            self.tetha = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
            self.w = [
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            ]
        else:
            self.N = N
            self.y = []
            self.x = []
            self.tetha = []
            self.w = []
            
            for i in range(0, self.N):
                self.y.append(0)
                self.x.append(0)
                self.tetha.append(0)
                
            for j in range(0, self.N):
                for i in range(0, self.N):
                    self.w.append(0)

        self.rng = []

    def _ijtok(self, i, j):
        return j * self.N + i

        
    def net(self, j):
        sum = 0
        for i in range(0, self.N):
            sum += self.w[self._ijtok(i,j)] * self.y[i] - self.tetha[i] + self.x[i]
        return sum
        
        
    def sgn(self, x):
        if x > 0:
            return 1
        else:
            return -1

    def range_init(self):
        self.rng = range(0, self.N)

    def clear_input(self):
        for i in range(0, self.N):
            self.x[i] = 0
        
    def set_input(self, x):
        self.x = x
        
    def calculate(self):
        for i in range(0, self.N):
            k = random.choice(self.rng)
            list(self.rng).pop(self.rng.index(k))
            self.y[k] = self.sgn(self.net(k))
        
        
    def itterate(self, epochs):
        for i in range(0, epochs):
            self.range_init()
            self.calculate()
            self.clear_input()
            print(self.y)

            
    def set_random_w_tetha(self):
        for j in range(0, self.N):
            for i in range(0, self.N):
                if i == j:
                    self.w[self._ijtok(i,j)] = 0
                else:
                    self.w[self._ijtok(i,j)] = random.uniform(-1, 1)
                    self.w[self._ijtok(j,i)] = self.w[self._ijtok(i,j)]
            self.tetha[j] = random.uniform(-0.1, 0.1)
            
            
    def set_random_input(self):
        for i in range(0, self.N):
            if random.uniform(-1, 1) > 0:
                self.x[i] = 1
            else:
                self.x[i] = -1
            
            
    def get_input(self):
        return self.x
            

    def get_output(self):
        return self.y
            
if __name__ == '__main__':
    nn = HopfieldNeuralNetwork(N=30)
    nn.set_random_w_tetha()
    nn.set_random_input()
    print(nn.x)
    nn.itterate(10)
















