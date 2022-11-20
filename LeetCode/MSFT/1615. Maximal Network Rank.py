# https://leetcode.com/problems/maximal-network-rank/
import itertools
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n, roads):
        degree_val = defaultdict(int)
        all_edges = set()

        for road in roads:
            degree_val[road[0]] += 1
            degree_val[road[1]] += 1
            all_edges.add(tuple(road))
            all_edges.add(tuple(road[::-1]))

        degree_val = {k: v for k, v in sorted(degree_val.items(), key=lambda x: x[1], reverse=True)}
        max_rank = 0
        for pair in itertools.permutations(degree_val.keys(), 2):
            if pair in all_edges or pair[::-1] in all_edges:
                current_rank = degree_val[pair[0]] + degree_val[pair[1]] - 1
            else:
                current_rank = degree_val[pair[0]] + degree_val[pair[1]]
            max_rank = max(max_rank, current_rank)
        return max_rank


if __name__ == '__main__':
    n = 4
    roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
    print(Solution().maximalNetworkRank(n, roads))

    n = 5
    roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
    print(Solution().maximalNetworkRank(n, roads))

    n = 8
    roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
    print(Solution().maximalNetworkRank(n, roads))
