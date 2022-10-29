# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            str_num = str(num)
            num = 0
            for s in str_num:
                num += int(s)
        return num


if __name__ == '__main__':
    num = 38
    print(Solution().addDigits(num))
