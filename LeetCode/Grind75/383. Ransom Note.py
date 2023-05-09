# https://leetcode.com/problems/ransom-note/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote, magazine):
        diff = set(ransomNote).difference(set(magazine))
        if diff:
            return False

        mag = Counter(magazine)
        note = Counter(ransomNote)

        for letter, number in note.items():
            if mag[letter] < number:
                return False
        return True


if __name__ == '__main__':
    ransomNote = "bbe"
    magazine = "abbbb"
    print(Solution().canConstruct(ransomNote, magazine))