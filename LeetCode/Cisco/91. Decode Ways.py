# https://leetcode.com/problems/decode-ways/

import string
from functools import lru_cache


class Solution:
    def __init__(self):
        self.map = {
            str(v): k for k, v in zip(string.ascii_lowercase, range(1, len(string.ascii_lowercase) + 1, 1))
        }

    def numDecodings(self, s):
        if len(s) == 0:
            return s

        if len(s) == 1:
            if self.map.get(s[0]):
                total = 1
            else:
                total = 0
        else:
            total = self.find_map_match(s)
        return total

    @lru_cache(None)
    def find_map_match(self, s):
        if len(s) >= 1 and s[0] == '0':
            return 0
        if len(s) == 1 or s == "":
            return 1

        if self.map.get(s[0: 0 + 2]):
            return self.find_map_match(s[1:]) + self.find_map_match(s[2:])
        else:
            return self.find_map_match(s[1:])


if __name__ == '__main__':
    s = "0"

    print(s)
    obj = Solution()
    print(obj.numDecodings(s))
