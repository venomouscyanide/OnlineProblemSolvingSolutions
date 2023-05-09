# https://leetcode.com/problems/first-bad-version/description/

version = 0


def isBadVersion(n):
    global version
    return n >= version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # numbers = list(range(1, n + 1, 1))

        left = 0
        right = n - 1

        last_bad = n

        while left <= right:
            mid = (left + right) // 2

            if last_bad == mid:
                return last_bad

            bad = isBadVersion(mid)
            if not bad:
                left = mid + 1
            else:
                right = mid - 1
                last_bad = mid

        return last_bad


if __name__ == '__main__':
    version = 3
    print(Solution().firstBadVersion(10))
