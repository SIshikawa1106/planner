import kdtree
from collections import deque
import numpy as np

DEBUG_VIEW = True

class Tree(object):
    def __init__(self, node):
        self.root = node
        self.node_list = node[np.newaxis, :]
        self._tree = kdtree.create([node], dimensions=node.size)

    def get_root(self):
        return self.root

    def add_node(self, node):
        self._tree.add(node)
        self.node_list = np.append(self.node_list, node[np.newaxis,:], axis=0)

    def find_nearest_node(self, target_node):
        nearest_node = self._tree.search_nn(target_node)
        if DEBUG_VIEW:
            print(nearest_node)
        return nearest_node[0].data

    def get_node_list(self):
        return self.node_list

if __name__ == "__main__":
    import numpy as np
    import sys, os


    sys.path.append("../")
    import Plot3DViewer

    print("TEST")

    node_tree = None

    for n in range(100):
        node = np.random.rand(3)

        if node_tree is None:
            node_tree = Tree(node)
        else:
            node_tree.add_node(node=node)

        points = node_tree.get_node_list()
        Plot3DViewer.Plot_3D(node_tree.get_node_list(), pause_time=0.1)

