# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board, word) -> bool:
        found = False
        self.row_limit = len(board)
        self.col_limit = len(board[0])
        for row in range(self.row_limit):
            for col in range(self.col_limit):
                found = self.check_if_found(board, row, col, word)
                if found:
                    return found
        return found

    def check_if_found(self, board, row, col, suffix_to_match):
        if not suffix_to_match:
            return True

        if row < 0 or row == self.row_limit or col < 0 or col == self.col_limit or \
                board[row][col] != suffix_to_match[0]:
            return False

        board[row][col] = "$"
        for row_dir, col_dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            found = self.check_if_found(board, row + row_dir, col + col_dir, suffix_to_match[1:])
            if found:
                return True
        board[row][col] = suffix_to_match[0]

        return False


if __name__ == '__main__':
    board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
    word = "AAAAAAAAAAAAABB"

    print(Solution().exist(board, word))
