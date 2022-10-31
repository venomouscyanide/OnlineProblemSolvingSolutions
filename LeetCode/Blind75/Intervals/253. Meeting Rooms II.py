# https://leetcode.com/problems/meeting-rooms-ii/
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        prio_q = [sorted_intervals[0][-1]]
        heapq.heapify(prio_q)

        for interval in sorted_intervals[1:]:
            end_time = prio_q[0]
            if interval[0] < end_time:
                heapq.heappush(prio_q, interval[-1])
            else:
                heapq.heappop(prio_q)
                heapq.heappush(prio_q, interval[-1])

        total_necessary = len(prio_q)
        return total_necessary


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(Solution().minMeetingRooms(intervals))

    intervals = [[7, 10], [2, 4]]
    print(Solution().minMeetingRooms(intervals))

    intervals = [[6, 15], [13, 20], [6, 17]]
    print(Solution().minMeetingRooms(intervals))