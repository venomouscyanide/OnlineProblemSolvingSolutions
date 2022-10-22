# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid):
        self.grid = grid

        num_islands = 0

        self.num_rows = len(grid)
        self.num_cols = len(grid[0])

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.grid[i][j] == '1':
                    num_islands += 1
                    self.backtrack(i, j)
        return num_islands

    def backtrack(self, row, col):

        self.grid[row][col] = '0'
        for update_row, update_col in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            new_row = row + update_row
            new_col = col + update_col
            if new_col < 0 or new_col > self.num_cols - 1 or new_row < 0 or new_row > self.num_rows - 1:
                continue
            elif self.grid[new_row][new_col] == '0':
                continue
            else:
                self.backtrack(new_row, new_col)


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))
