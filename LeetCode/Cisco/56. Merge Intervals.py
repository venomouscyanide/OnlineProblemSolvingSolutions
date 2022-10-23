# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals_array):
        intervals_array.sort(key=lambda x: x[0], reverse=False)

        new_intervals = []
        new_intervals.append(intervals_array[0])

        for interval in intervals_array[1:]:
            if new_intervals[-1][-1] >= interval[0] and new_intervals[-1][-1] >= interval[0]:
                if interval[-1] <= new_intervals[-1][-1]:
                    new_intervals[-1] = [new_intervals[-1][0], new_intervals[-1][-1]]
                else:
                    new_intervals[-1] = [new_intervals[-1][0], interval[-1]]
            else:
                if interval != new_intervals[-1]:
                    new_intervals.append(interval)

        return new_intervals


if __name__ == '__main__':
    intervals = [[1, 4], [2, 3]]
    print(Solution().merge(intervals))

    intervals = [[1, 4], [1, 4]]
    print(Solution().merge(intervals))

    intervals = [[1, 4], [0, 4]]
    print(Solution().merge(intervals))

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))
