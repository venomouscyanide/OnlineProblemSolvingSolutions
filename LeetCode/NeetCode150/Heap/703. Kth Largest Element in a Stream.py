# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums

    def __repr__(self):
        return str(self.nums)

    def add(self, val: int):
        if not self.nums or len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val >= self.nums[0]:
            heapq.heapreplace(self.nums, val)

        return self.nums[0]


if __name__ == '__main__':
    largest = KthLargest(3, [9, 8, 7])
    print(largest.add(3))
    print(largest.add(4))
    print(largest.add(2))
