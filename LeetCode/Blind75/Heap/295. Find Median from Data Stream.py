# https://leetcode.com/problems/find-median-from-data-stream/
import heapq


class MedianFinder:

    def __init__(self):
        self.nums = []
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)
        elif len(self.min_heap) - len(self.max_heap) > 1:
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return - self.max_heap[0]
        else:
            return (self.min_heap[0] + -1 * self.max_heap[0]) / 2


if __name__ == '__main__':
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()

    # obj.addNum(1)
    # obj.addNum(2)
    # obj.addNum(3)
    obj.addNum(-1)
    obj.addNum(-2)
    obj.addNum(-3)
    obj.addNum(-4)

    print(obj.findMedian())
