import numpy as np

from collections import deque

class CollisionDetector:
    collision_resolution = 1

    def __init__(self, env):
        self.env = env

    def isCollidedPoint(self, point):
        return self.env[point[0],point[1],point[2]]

    def isCollidedPath(self, start, end):

        size = (start - end)
        max_size = max(abs(size))
        step_size = size / max_size

        # TODO : binary tree search
        tmp_point = start
        for n in range(max_size + 1):
            if self.isCollidedPoint(np.ceil(tmp_point).astype(int)):
                return True

            tmp_point = tmp_point + step_size

        tmp_points = deque()
        tmp_points.append(((start + end)*0.5, start, end))
        while len(tmp_points)>0:
            points = tmp_points.popleft()
            p


        return False


if __name__ == "__main__":
    env = np.random.rand(1000).reshape((10,10,10))

    env = env > 0.5

    collision_detector = CollisionDetector(env)
    point = np.random.randint(0, 10, 3)

    clded = collision_detector.isCollidedPoint(point)

    print(clded)

    start = np.array([0, 0, 1])
    end = np.array([8, 3, 5])

    clded = collision_detector.isCollidedPath(start, end)

    print(clded)
