# https://leetcode.com/problems/maximum-population-year/
import math
from collections import defaultdict


class Solution:
    def maximumPopulation(self, logs):
        if not logs:
            return

        overlaps_dict = defaultdict(int)
        for interval in logs:
            range_of_intervals = range(interval[0], interval[-1])
            for year in range_of_intervals:
                overlaps_dict[year] += 1

        sorted_overlaps = sorted(overlaps_dict.items(), key=lambda x: (x[1]), reverse=True)
        largest = sorted_overlaps[0][-1]

        lowest_year = math.inf
        for year, occ in sorted_overlaps:
            if occ < largest:
                continue
            if year < lowest_year:
                lowest_year = year

        return lowest_year


if __name__ == '__main__':
    logs = [[2008, 2026], [2004, 2008], [2034, 2035], [1999, 2050], [2049, 2050], [2011, 2035], [1966, 2033],
            [2044, 2049]]
    print(Solution().maximumPopulation(logs))

    logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
    print(Solution().maximumPopulation(logs))

    logs = [[1950, 1961], [2000, 2005], [2004, 2005], [2100, 2010], [10, 20], [10, 20], [10, 30], [10, 40]]
    print(Solution().maximumPopulation(logs))
