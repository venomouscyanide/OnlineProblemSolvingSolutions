# https://leetcode.com/problems/cinema-seat-allocation/
# with help from: https://leetcode.com/problems/cinema-seat-allocation/discuss/552211/Python-Very-concise-solution-using-hash-map
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        seat_dict = defaultdict(set)
        counter = 2 * n

        for i, j in reservedSeats:
            i = i - 1
            j = j - 1

            if 1 <= j <= 4:
                seat_dict[i].add(1)

            if 3 <= j <= 6:
                seat_dict[i].add(11)

            if 5 <= j <= 8:
                seat_dict[i].add(111)

        for occupancy in seat_dict.values():
            if len(occupancy) == 3:
                counter -= 2
            else:
                counter -= 1

        return counter


if __name__ == '__main__':
    n = 3
    reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 4

    n = 2
    reservedSeats = [[2, 1], [1, 8], [2, 6]]
    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 2

    n = 4
    reservedSeats = [[4, 3], [1, 4], [4, 6], [1, 7]]
    assert Solution().maxNumberOfFamilies(n, reservedSeats) == 4
