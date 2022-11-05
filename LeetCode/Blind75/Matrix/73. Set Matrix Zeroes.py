# https://leetcode.com/problems/set-matrix-zeroes/
import copy


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])

        original_matrix = copy.deepcopy(matrix)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if original_matrix[i][j] == 0:
                    self.dfs(i, j, (i, j), matrix, prefix=f"${(i,j)}")

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if str(matrix[i][j]).startswith("$"):
                    matrix[i][j] = 0

    def dfs(self, i, j, og_tuple, matrix, prefix):

        if (og_tuple[0] == i or og_tuple[-1] == j) and matrix[i][j] != prefix:
            matrix[i][j] = prefix
        else:
            return

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dir in dirs:
            new_i = i + dir[0]
            new_j = j + dir[-1]
            if new_i < 0 or new_j < 0 or new_i == self.num_rows or new_j == self.num_cols:
                continue
            self.dfs(new_i, new_j, og_tuple, matrix, prefix)

        return


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    print(matrix)
    Solution().setZeroes(matrix)
    print(matrix, '\n\n')

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(matrix)
    Solution().setZeroes(matrix)
    print(matrix, '\n\n')

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(matrix)
    Solution().setZeroes(matrix)
    print(matrix, '\n\n')
