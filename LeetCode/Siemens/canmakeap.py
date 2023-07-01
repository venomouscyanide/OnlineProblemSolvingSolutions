from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        zipp = [(arr[i], arr[i + 1]) for i in range(0, len(arr) - 1)]

        diff = zipp[0][1] - zipp[0][0]
        for i, j in zipp[1:]:
            if diff != j - i:
                return False

        return True


if __name__ == '__main__':
    arr = [3, 5, 1]
    print(Solution().canMakeArithmeticProgression(arr))

    arr = [1, 2, 4]
    print(Solution().canMakeArithmeticProgression(arr))
