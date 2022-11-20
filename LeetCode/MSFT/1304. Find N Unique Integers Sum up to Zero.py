# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n):
        array = [0 for _ in range(n)]
        count = -1
        summation = 0

        for index in range(n - 1):
            array[index] = count
            count -= 1
            summation += array[index]
        array[-1] = -summation


if __name__ == '__main__':
    Solution().sumZero(5)
    Solution().sumZero(1)
    Solution().sumZero(2)
    Solution().sumZero(6)
