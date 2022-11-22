# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/


class Solution:
    def numSteps(self, s: str) -> int:
        integer = eval('0' + 'b' + s)

        count = 0
        while integer != 1:
            if integer % 2 == 0:
                integer = integer // 2
            else:
                integer = integer + 1
            count += 1

        return count
