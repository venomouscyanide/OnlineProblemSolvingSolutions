# https://leetcode.com/problems/spiral-matrix/
# completed with help from Solution 2.

class Solution:
    def spiralOrder(self, matrix):
        seen = set()

        row, col = 0, 0

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        num_elements = num_cols * num_rows

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        traversed_matrix = [matrix[row][col]]
        seen.add((row, col))
        current_dir = 0

        while len(traversed_matrix) < num_elements:
            while True:
                new_row = row + directions[current_dir][0]
                new_col = col + directions[current_dir][1]

                if new_row < 0 or new_col >= num_cols or new_row >= num_rows or new_col < 0:
                    break

                if (new_row, new_col) not in seen:
                    row, col = new_row, new_col
                    seen.add((row, col))
                    value = matrix[row][col]
                    traversed_matrix.append(value)
                else:
                    break
            current_dir = (current_dir + 1) % 4

        return traversed_matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
