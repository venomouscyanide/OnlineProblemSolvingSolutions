# https://leetcode.com/problems/longest-palindrome/editorial/
from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        palindromes = 0
        for counter in Counter(s).values():
            palindromes += counter // 2 * 2
            if counter % 2 == 1 and palindromes % 2 == 0:
                palindromes += 1
        return palindromes


if __name__ == '__main__':
    s = "abccccdd"
    print(Solution().longestPalindrome(s))
