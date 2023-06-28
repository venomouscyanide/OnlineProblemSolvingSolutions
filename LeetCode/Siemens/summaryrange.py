import math
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums

        check = nums[0]
        output = []
        lower_bound = check

        nums.append(math.inf)
        for index, num in enumerate(nums[1:], start=1):
            diff = num - check
            if diff > 1:
                if lower_bound != nums[index - 1]:
                    rangge = f"{lower_bound}->{nums[index - 1]}"
                else:
                    rangge = f"{lower_bound}"
                check = num
                lower_bound = num
                output.append(rangge)
            else:
                check = num

        return output


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(nums))
