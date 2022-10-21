# https://leetcode.com/problems/word-search-ii/


class TrieStorage:
    def __init__(self):
        self.word = False
        self.actual_word = ""
        self.children = {}

    def __repr__(self):
        return f'{self.children}'


class Trie:
    def __init__(self):
        self.root = TrieStorage()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                new_node = TrieStorage()
                node.children[w] = new_node
                node = new_node
        node.word = True
        node.actual_word = word

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False

        return True if node.word else False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return False

        return True


class Solution:
    def findWords(self, board, words):
        self.matches = []
        self.num_rows = len(board)
        self.num_cols = len(board[0])

        trie = Trie()

        for word in words:
            trie.insert(word)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.backtrack(board, i, j, trie.root)

        return list(self.matches)

    def backtrack(self, board, i, j, node):
        letter = board[i][j]
        parent = None
        if node.children.get(letter):
            parent = node
            node = node.children[letter]

        if node.word:
            node.word = False
            self.matches.append(node.actual_word)

        board[i][j] = '%'
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row = i + dir[0]
            new_col = j + dir[-1]

            if new_row >= self.num_rows or new_col >= self.num_cols or new_col < 0 or new_row < 0:
                continue
            if not board[new_row][new_col] in node.children:
                continue
            self.backtrack(board, new_row, new_col, node)

        if not node.children and parent:
            parent.children.pop(letter)
        board[i][j] = letter


if __name__ == '__main__':
    board = [["a", "a"]]
    words = ["a"]
    print(Solution().findWords(board, words))

    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution().findWords(board, words))

    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    print(Solution().findWords(board, words))

    board = [["o", "a", "a", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
    words = ["oa", "oaa"]
    print(Solution().findWords(board, words))
