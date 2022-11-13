# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
from collections import defaultdict


class Solution:
    def countComponents(self, n, edges):
        seen = set()

        adj_list = defaultdict(list)

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        all_unique_nodes = set()
        for edge in edges:
            all_unique_nodes.add(edge[0])
            all_unique_nodes.add(edge[1])

        num_components = 0
        while all_unique_nodes:
            start = all_unique_nodes.pop()
            stack = [start]
            num_components += 1

            while stack:
                curr_node = stack.pop(-1)
                neighs = adj_list[curr_node]
                if curr_node not in seen:
                    seen.add(curr_node)
                    if curr_node in all_unique_nodes:
                        all_unique_nodes.remove(curr_node)
                    stack.extend(neighs)
                else:
                    continue
        return num_components + (n - len(seen))


if __name__ == '__main__':
    n = 10
    edges = [[0, 1], [1, 2], [3, 4]]
    print(Solution().countComponents(n, edges))

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(Solution().countComponents(n, edges))

    n = 4
    edges = [[2, 3], [1, 2], [1, 3]]
    print(Solution().countComponents(n, edges))
