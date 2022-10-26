# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        num_ones = 0
        for i in str(n):
            if i == '1':
                num_ones += 1
        return num_ones


if __name__ == '__main__':
    n = 11
    print(Solution().hammingWeight(n))