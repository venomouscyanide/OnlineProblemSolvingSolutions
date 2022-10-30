# https://leetcode.com/problems/meeting-rooms/
class Solution:
    def canAttendMeetings(self, intervals):
        can_attend = True
        if not intervals:
            return can_attend

        sorted_intervals = sorted(intervals, key=lambda x: x[-1])
        prev = sorted_intervals[0]

        for interval in sorted_intervals[1:]:
            if interval[0] < prev[-1]:
                return False
            prev = interval
        return can_attend


if __name__ == '__main__':
    intervals = [[7, 10], [2, 4]]
    print(Solution().canAttendMeetings(intervals))
