"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""
from collections import defaultdict
from itertools import combinations


def sherlocks_anagrams(org_string):
    string = list(org_string)
    counter = defaultdict(int)
    summation = 0
    for i, j in combinations(range(len(string) + 1), 2):
        key = ''.join(sorted(string[i:j]))
        if not counter[key]:
            counter[key] = 1
        else:
            summation += counter[key]
            counter[key] += 1
    return summation


if __name__ == '__main__':
    print(sherlocks_anagrams('abba'))
    print(sherlocks_anagrams('kkkk'))
