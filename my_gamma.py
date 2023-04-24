import numpy as np


class MyGamma:
    def __init__(self, shape=1., loc=0., scale=1., data=None, mode='custom'):
        if data is None:
            data = []
        self.shape = shape
        self.loc = loc
        self.scale = scale
        self.data = data
        self.mode = mode

    def generate(self, n=1):
        if self.mode == 'custom':
            return self.custom_gamma(n)
        else:
            return np.random.default_rng(0).gamma(shape=self.shape, scale=self.scale, size=n) + self.loc

    def custom_gamma(self, n):
        rngs = []
        k = self.shape / 10
        theta = self.scale / 10
        while len(rngs) < n:
            u1 = np.random.uniform(0, 1)
            u2 = np.random.uniform(0, 1)
            v = np.log(u1 / (1 - u1))
            x = k * np.power(np.exp(1), v)
            if u2 <= np.power(x / (k * theta), self.shape - 1) * np.exp(-x / (k * theta)):
                rngs.append(x * 10 + self.loc)
        return rngs

    def get_one(self):
        return self.generate()[0]
