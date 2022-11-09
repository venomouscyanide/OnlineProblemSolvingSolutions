# https://leetcode.com/problems/graph-valid-tree/
from collections import defaultdict


class Solution:
    def validTree(self, n, edges):
        if not edges and n == 1:
            return True
        if not edges and n > 1:
            return False

        loop = False

        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        seen = set()
        start = list(graph.keys())[0]
        stack = [start]

        while len(stack) > 0:
            current_node = stack.pop(-1)

            if current_node in seen:
                loop = True
                break

            # print(f"Processed {current_node}")
            neighbors = graph[current_node]
            seen.add(current_node)
            if not neighbors:
                continue
            stack.extend(neighbors)
            for neigh in neighbors:
                if current_node in graph[neigh]:
                    graph[neigh].remove(current_node)
        return not loop and len(seen) == n


if __name__ == '__main__':
    n = 4
    edges = [[0, 1], [2, 3]]
    print(Solution().validTree(n, edges))

    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(Solution().validTree(n, edges))

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 4]]
    print(Solution().validTree(n, edges))

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(Solution().validTree(n, edges))
