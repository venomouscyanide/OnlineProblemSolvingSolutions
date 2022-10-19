# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieStorage:
    def __init__(self):
        self.word = False
        self.children = {}


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


if __name__ == '__main__':
    word = "doggo"
    prefix = "d"

    obj = Trie()
    print(obj.insert(word))
    print(obj.search("dog"))
    print(obj.search("dogg"))
    print(obj.search("www"))
    print(obj.search("doggo"))
    print(obj.startsWith("do"))
