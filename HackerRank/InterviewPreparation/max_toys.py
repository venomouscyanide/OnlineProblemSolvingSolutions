def max_toys(prices, max_total):
    prices.sort()
    total_so_far = 0
    counter = 0
    # print(prices)
    for price in prices:
        total_so_far += price
        if total_so_far > max_total:
            break
        else:
            counter += 1
    # print(total_so_far, counter)
    return counter


if __name__ == '__main__':
    max_toys([1, 12, 5, 111, 200, 1000, 10], 50)
    max_toys([1, 2, 3, 4], 7)
    max_toys([1, 12, 5, 111, 200, 1000, 10], 1)
