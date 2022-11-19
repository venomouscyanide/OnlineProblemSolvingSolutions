# https://leetcode.com/problems/ugly-number/


class Solution:
    def isUgly(self, n: int) -> bool:

        factors = [2, 3, 5]

        def _check_factor(factor, n, prev):
            if n % factor == 0:
                return n // factor
            return n

        prev = -1
        factor = factors.pop()
        while 1:
            n = _check_factor(factor, n, prev)

            if n == prev:
                if factors:
                    factor = factors.pop()
                else:
                    return False

            prev = n
            if n == 1:
                return True


if __name__ == '__main__':
    print(Solution().isUgly(16))
    print(Solution().isUgly(1))
    print(Solution().isUgly(21))
