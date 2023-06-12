import unittest

import networkx as nx

from LeetCode.Siemens.searching.bfs_dfs import dfs, bfs


class TestBFSDFS(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = nx.erdos_renyi_graph(12, 0.25, seed=42)

    def testDFS(self):
        self.assertListEqual([0, 2, 4, 8, 10, 11, 5, 9, 1, 7, 6, 3], bfs(self.graph, 0))

    def testBFS(self):
        self.assertListEqual([0, 11, 10, 7, 6, 5, 1, 3, 8, 4, 9, 2], dfs(self.graph, 0))


if __name__ == '__main__':
    unittest.main()
