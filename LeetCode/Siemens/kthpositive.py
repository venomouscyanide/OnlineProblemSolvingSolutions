from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lp = 0
        counter = 1
        missing_list = []

        while lp < len(arr):
            if arr[lp] < 1:
                lp += 1
            else:
                if counter != arr[lp]:
                    missing_list.append(counter)
                else:
                    lp += 1
                counter += 1

        if k > len(missing_list):
            return arr[-1] + k - len(missing_list)
        else:
            return missing_list[k - 1]
