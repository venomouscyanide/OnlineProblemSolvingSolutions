# https://leetcode.com/problems/contains-duplicate/
from collections import defaultdict


def run(nums):
    counter = defaultdict(int)

    for cand in nums:
        counter[cand] += 1

    for value in counter.values():
        if value > 1:
            return True

    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    run(nums)
