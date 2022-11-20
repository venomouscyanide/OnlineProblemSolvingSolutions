# https://leetcode.com/problems/design-add-and-search-words-data-structure/
from collections import defaultdict


class TrieChar:
    def __init__(self, char):
        self.char = char
        self.is_word = False

    def __repr__(self):
        return f"{self.char}"


class WordDictionary:
    def __init__(self):
        self.trie = defaultdict(dict)

    def _add_word(self, word):
        trie_char = self.trie
        num_char = len(word)
        for index, char in enumerate(word):
            if trie_char.get(char):
                trie_char = trie_char[char]
            else:
                trie_char[char] = {}
                trie_char = trie_char[char]

            if index == num_char - 1:
                trie_char.update({"is_word": True})

    def addWord(self, word):
        self._add_word(word)

    def _search_helper(self, trie, word):
        if not word:
            if trie.get('is_word'):
                self.result = True
            return

        if word[0] == ".":
            for child in trie.values():
                if type(child) == bool:
                    continue
                self._search_helper(child, word[1:])
        else:
            trie = trie.get(word[0])
            if not trie:
                return
            return self._search_helper(trie, word[1:])
        return

    def search(self, word):
        self.result = False
        self._search_helper(self.trie, word)
        return self.result


if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("a")
    obj.addWord("a")
    print(obj.search("a."))
    obj.addWord("heyy")
    obj.addWord("hey")
    obj.addWord("aa")
    print(obj.search("..y"))
    print(obj.search(".a"))
    print(obj.search("..y.."))
    print(obj.search("..y"))
    print(obj.search("h.w"))
    print(obj.search("..y."))
    print(obj.search("aa"))
    obj.addWord("aa")
    print(obj.search(".a"))
