import numpy as np

class Smoother:
    def __init__(self, collision_detector, max_count=10**2, min_improvement_rate=1.0e-3):
        self._max_count = max_count
        self._min_improvement_rate = min_improvement_rate
        self._collision_detector = collision_detector

    def run(self, path):

        for n in range(self._max_count):
            improvement_rate, new_path = self._optimize(path)

            if improvement_rate is None:
                continue

            path = new_path

            if improvement_rate<self._min_improvement_rate:
                break

        return path

    def _optimize(self, path):
        pass
        improvement_rate = 0
        return improvement_rate

    def _cald_dist(self, path):
        delta = np.array([np.linalg.norm(path[n + 1] - path[n]) for n in range(len(path) - 1)])
        return np.sum(delta), delta

    def _insert_new_path(self, original, new_path, insert_indexes):

        original = np.delete(original, slice(min(insert_indexes), max(insert_indexes), None), axis=0)
        original = np.insert(original, insert_indexes[0], new_path, axis=0)

class RandomCutSmoother(Smoother):
    def _optimize(self, path):
        dist, delta_dist = self._cald_dist(path)

        idx = np.random.choice(np.arange(len(path)-1), 2, replace=False)

        rand_dists = np.random.rand(2)

        #p1 = (path[idx[0]+1,:] - path[idx[0],:]) * rand_dists[0] / delta_dist[idx[0]] + path[idx[0],:]
        #p2 = (path[idx[1]+1,:] - path[idx[1],:]) * rand_dists[1] / delta_dist[idx[1]] + path[idx[1],:]

        p1 = self._create_new_point(path[idx[0] + 1, :], path[idx[0], :], delta_dist[idx[0]])
        p2 = self._create_new_point(path[idx[1] + 1, :], path[idx[1], :], delta_dist[idx[1]])

        #if self._collision_detector.isCollidedPath(p1, p2) == True:
        #    return None

        #new = np.delete(path, )


    def _create_new_point(self, p1, p2, dist):
        return (p2 - p1) * np.random.rand() / dist + p1

if __name__ == "__main__":

    import matplotlib.pyplot as plt
    from collections import deque
    import itertools

    np.random.seed(0)
    path = np.empty((0,2))

    for n in range(20):
        plt.cla()
        p = np.random.rand(2)
        path = np.append(path, p[np.newaxis,:], axis=0)

        #print(path)

    print(len(path))
    plt.scatter(path[:,0], path[:,1])
    plt.plot(path[:,0], path[:,1])
    plt.scatter(path[0,0], path[0,1], c='r')
    plt.scatter(path[-1, 0], path[-1, 1], c='r')

    delta = np.array([np.linalg.norm(path[n+1] - path[n]) for n in range(len(path)-1)])

    print(path[np.random.randint(0, len(path)),:])
    #plt.show()

    for i in range(10):
        idx =  np.random.choice(np.arange(len(path)-1), 2, replace=False)
        print(idx)

    #print(path)
    idx =  np.random.choice(np.arange(len(path)-1), 2, replace=False)
    #print(idx)

    def delete(path, start, end):
        path = np.delete(path, [start, end], axis=0)


    print("test")
    path = np.arange(0, 20).reshape((10,2))
    print(path)

    new_path = np.full((2,2), -1, dtype=int)
    print("new path\n", new_path)

    idx = np.random.randint(0, len(path), size=2)
    print("index :", idx)

    range = [min(idx),max(idx)]
    print("range :", np.s_[min(idx):max(idx)])
    path = np.delete(path, np.s_[min(idx):max(idx)], axis=0)
    print("delete\n", path)

    new_path = np.insert(path, min(idx), new_path, axis=0)
    print("insert new path\n", new_path)

