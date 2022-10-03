# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import defaultdict


def run(s):
    if not s:
        return 0

    check = defaultdict(int)
    lp = 0
    rp = 1

    check[s[lp]] += 1
    largest = 1
    while lp < len(s) - 1 and rp < len(s):
        if check[s[rp]] > 0:
            lp += 1
            rp = lp + 1
            largest = max(largest, len(check.keys()))
            check = defaultdict(int)
            check[s[lp]] += 1
            continue

        check[s[rp]] += 1
        rp += 1

    largest = max(largest, len(check.keys()))
    return largest


if __name__ == '__main__':
    s = "dvdf"
    print(run(s))

    s = "abcabcbb"
    print(run(s))

    s = "bbbbb"
    print(run(s))

    s = "pwwkew"
    print(run(s))

    s = "p"
    print(run(s))
