# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights):
        self.num_rows = len(heights)
        self.num_cols = len(heights[0])

        paths = []
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                seen = set()

                seen = self.dfs(heights, i, j, seen, heights[i][j])
                if len(seen) == 2:
                    paths.append([i, j])

        return paths

    def dfs(self, heights, i, j, seen, prev):
        if heights[i][j] == '$':
            return seen

        if heights[i][j] > prev:
            return seen

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        prev = heights[i][j]
        heights[i][j] = '$'

        if i == 0 or j == 0:
            seen.add(1)

        if j == self.num_cols - 1 or i == self.num_rows - 1:
            seen.add(0)

        if len(seen) == 2:
            heights[i][j] = prev
            return seen

        for dir in dirs:
            new_i = dir[0] + i
            new_j = dir[-1] + j

            if new_j >= self.num_cols or new_j < 0 or new_i >= self.num_rows or new_i < 0:
                continue
            self.dfs(heights, new_i, new_j, seen, prev)

        heights[i][j] = prev

        return seen


if __name__ == '__main__':
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(Solution().pacificAtlantic(heights))
