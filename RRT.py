import numpy as np
from Environment import CollisionDetector

class Normalizer:
    def __init__(self, max_value, min_value, less=False, more=True):
        self._max = max_value
        self._min = min_value
        self._range = max_value - min_value
        self._less = less
        self._more = more

    def encode(self, value):
        value = (value - self._min ) / (self._range)
        return value

    def decode(self, value):
        value = (value * self._range) + self._min

        if self._more is False:
            value = np.where(value>=self._max, value-1e-7, value)
        if self._less is False:
            value = np.where(value<=self._min, value+1e-7, value)

        return value

class RRT:
    def __init__(self, collision_detector):
        self._collision_detector = collision_detector
        self._normalizer = Normalizer()


if __name__=="__main__":
    env = np.random.rand(1000).reshape((10,10,10))
    env = env > 0.9
    collision_detector = CollisionDetector(env)

    test = np.random.rand(5)
    print(test)

    test = np.where(test>0.5, 0.5, test)
    print(test)

    normalizer = Normalizer(max_value=np.array([10,10,10]),min_value=np.array([0,0,0]))
    #for n in range(10):

