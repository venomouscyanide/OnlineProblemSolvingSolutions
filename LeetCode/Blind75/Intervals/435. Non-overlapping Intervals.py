# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: (x[0]))

        merged_intervals = [sorted_intervals[0]]

        counter = 0
        for interval in sorted_intervals[1:]:
            if interval[0] < merged_intervals[-1][-1]:
                counter += 1
                if interval[-1] < merged_intervals[-1][-1]:
                    merged_intervals[-1] = interval
            else:
                merged_intervals.append(interval)
        return counter


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(Solution().eraseOverlapIntervals(intervals))

    intervals = [[1, 2], [1, 2], [1, 2]]
    print(Solution().eraseOverlapIntervals(intervals))

    intervals = [[1, 2], [2, 3]]
    print(Solution().eraseOverlapIntervals(intervals))

    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    print(Solution().eraseOverlapIntervals(intervals))

    intervals = [[0, 1], [3, 4], [1, 2]]
    print(Solution().eraseOverlapIntervals(intervals))
