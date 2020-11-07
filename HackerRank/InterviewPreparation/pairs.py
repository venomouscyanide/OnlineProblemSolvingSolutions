"""
https://www.hackerrank.com/challenges/sock-merchant/problem
"""
from collections import Counter


def pairs(n, list_of_items):
    count = Counter(list_of_items)
    number = [value // 2 for value in count.values()]
    summation = 0
    for item in number:
        summation += item
    return summation


if __name__ == '__main__':
    pairs(10, [10, 20, 20, 10, 10, 30, 50, 10, 20])
