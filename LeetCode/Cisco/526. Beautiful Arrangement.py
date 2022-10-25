# https://leetcode.com/problems/beautiful-arrangement/
# solved with major help from LC user: https://leetcode.com/problems/beautiful-arrangement/discuss/919426/Backtracking-python-solution

class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, n: int) -> int:
        self.nums = [i + 1 for i in range(n)]
        self.digit_checked = [False for _ in range(n)]

        def dfs(candidates):
            if len(candidates) == len(self.nums):
                self.count += 1

            for index, _ in enumerate(self.nums):
                new_index = len(candidates) + 1
                if not self.digit_checked[index] and \
                        (new_index % self.nums[index] == 0 or self.nums[index] % new_index == 0):
                    candidates.append(self.nums[index])
                    self.digit_checked[index] = True
                    dfs(candidates)
                    self.digit_checked[index] = False
                    candidates.pop()

        dfs([])

        return self.count


if __name__ == '__main__':
    print(Solution().countArrangement(5))
