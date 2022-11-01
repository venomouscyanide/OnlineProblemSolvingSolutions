# https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(self, intervals, newInterval):

        intervals.append(newInterval)
        sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=False)

        prev = sorted_intervals[0]
        merged_intervals = [prev]

        for interval in sorted_intervals[1:]:
            if interval[0] <= merged_intervals[-1][-1]:
                start = merged_intervals[-1][0]
                end = interval[-1] if interval[-1] >= merged_intervals[-1][-1] else merged_intervals[-1][-1]
                new_interval = [start, end]
                merged_intervals[-1] = new_interval
            else:
                merged_intervals.append(interval)

        return merged_intervals


if __name__ == '__main__':
    intervals = []
    newInterval = [2, 5]
    # expected [[1,5],[6,9]]
    print(Solution().insert(intervals, newInterval))

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    # expected [[1,2],[3,10],[12,16]]
    print(Solution().insert(intervals, newInterval))
