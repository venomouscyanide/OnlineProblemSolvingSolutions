from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums) -> int:
        counter = defaultdict(int)

        num_pairs = 0
        for num in nums:
            counter[num] += 1

            num_pairs += counter[num] - 1
        return num_pairs


if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    print(Solution().numIdenticalPairs(nums))
