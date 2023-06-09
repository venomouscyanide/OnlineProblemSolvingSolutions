import math

version = 0


def isBadVersion(n):
    global version
    return n >= version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        last_bad = n

        while left <= right:
            middle = (left + right) // 2

            if last_bad == middle:
                return last_bad

            if isBadVersion(middle):
                right = middle - 1
                last_bad = middle
            else:
                left = mid + 1

        return last_bad


if __name__ == '__main__':
    version = 1702766719
    print(Solution().firstBadVersion(n=2126753390))
