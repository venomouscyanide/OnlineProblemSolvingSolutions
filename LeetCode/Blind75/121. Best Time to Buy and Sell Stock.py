# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def run(prices):
    max_profit = 0

    lp = 0
    rp = 1

    tot = len(prices)
    while rp < tot:
        if prices[rp] > prices[lp]:
            profit = prices[rp] - prices[lp]

            if profit > max_profit:
                max_profit = profit
        else:
            # lowest so far is captured by lp
            lp = rp
        rp += 1

    return max_profit


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 1, 2, 5]
    print(run(prices))

    prices = [7, 6, 4, 3, 1]
    print(run(prices))
