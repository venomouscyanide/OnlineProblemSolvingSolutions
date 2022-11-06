# https://leetcode.com/problems/course-schedule/
from collections import defaultdict


class Solution:
    def canFinish(self, _, prerequisites):
        graph = defaultdict(list)

        for pre in prerequisites:
            graph[pre[-1]].append(pre[0])

        seen = set()
        nodes = list(graph.keys())
        for course in nodes:
            cycle = set()
            has_cycle = self.dfs(course, graph, seen, cycle)
            if has_cycle:
                return False
        return True

    def dfs(self, course, graph, seen, cycle):
        if cycle:
            if course in cycle:
                return True
        cycle.add(course)

        if course not in seen:
            seen.add(course)
        else:
            cycle.remove(course)
            return False

        has_cycle = False
        for neigh in graph.get(course, []):
            has_cycle = self.dfs(neigh, graph, seen, cycle)
            if has_cycle:
                return True
        cycle.remove(course)

        return has_cycle


if __name__ == '__main__':
    # True
    numCourses = 7
    prerequisites = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
    print(Solution().canFinish(numCourses, prerequisites))

    # False
    numCourses = 4
    prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
    print(Solution().canFinish(numCourses, prerequisites))

    # True
    numCourses = 2
    prerequisites = [[0, 4], [4, 2]]
    print(Solution().canFinish(numCourses, prerequisites))

    # False
    numCourses = 2
    prerequisites = [[0, 4], [4, 0]]
    print(Solution().canFinish(numCourses, prerequisites))

    # True
    numCourses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    print(Solution().canFinish(numCourses, prerequisites))
