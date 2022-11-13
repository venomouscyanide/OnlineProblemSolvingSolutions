# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split(" ")
        s_list = list(filter(lambda x: x, s_list))
        return " ".join(s_list[::-1])
