import math


class Solution:
    # 7 1 5 3 6 4
    def maxProfit(self, prices) -> int:
        peak = 0
        valley = math.inf

        for i in range(len(prices)):
            if prices[i] < valley:
                valley = prices[i]
            gain = prices[i] - valley
            if gain > peak:
                peak = gain
        return peak


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4, 122]))
