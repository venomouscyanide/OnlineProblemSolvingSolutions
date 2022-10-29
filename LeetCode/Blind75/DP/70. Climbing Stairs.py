# https://leetcode.com/problems/climbing-stairs/
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = tuple([0 for _ in range(n)])
        self.total = 0

        @lru_cache(None)
        def dfs(stairs, step):
            if step > len(stairs):
                return 0

            new_stairs = tuple(list(stairs[step:]))

            if not new_stairs:
                return 1

            return dfs(new_stairs, step=1) + dfs(new_stairs, step=2)

        ret = dfs(stairs, 0)
        return ret


if __name__ == '__main__':
    n = 5
    print(Solution().climbStairs(n))
