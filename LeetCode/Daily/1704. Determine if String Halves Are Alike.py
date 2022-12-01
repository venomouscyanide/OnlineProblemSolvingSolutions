# https://leetcode.com/problems/determine-if-string-halves-are-alike/
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        len_s = len(s)

        count_a = 0
        count_b = 0

        for i in range(len_s // 2):
            if s[i] in vowels:
                count_a += 1
            if s[i + len_s // 2] in vowels:
                count_b += 1

        if count_a != count_b:
            return False

        return True
