# https://leetcode.com/problems/longest-happy-string/
from collections import Counter


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # __| __| __|

        counter = Counter({
            "a": a,
            "b": b,
            "c": c
        })

        (most_common_one, _), (most_common_two, _) = counter.most_common(2)
        formed_string = ""

        most_common_counter = {
            "a": 0,
            "b": 0,
            "c": 0
        }

        while counter[most_common_two] and counter[most_common_one]:
            formed_string += ""

            if most_common_counter[most_common_one] != 2:
                formed_string += most_common_one
                counter[most_common_one] -= 1
                most_common_counter[most_common_one] += 1
                most_common_counter[most_common_two] = 0
            else:
                formed_string += most_common_two
                counter[most_common_two] -= 1
                most_common_counter[most_common_one] = 0
                most_common_counter[most_common_two] += 1

            (most_common_one, _), (most_common_two, _) = counter.most_common(2)

        while counter[most_common_one] and most_common_counter[most_common_one] != 2:
            formed_string += most_common_one
            counter[most_common_one] -= 1
            most_common_counter[most_common_one] += 1

        return formed_string


if __name__ == '__main__':
    print(Solution().longestDiverseString(7, 1, 0))
