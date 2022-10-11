# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import Counter, defaultdict


def run(s, k):
    lp = 0
    longest = 0
    counter = defaultdict(int)

    tot = len(s)
    for index in range(tot):
        counter[s[index]] += 1

        cell_count = index - lp + 1
        if cell_count - max(counter.values()) <= k: # need to replace this many
            longest = max(longest, cell_count)
        else:
            counter[s[lp]] -= 1
            lp += 1

    return longest


if __name__ == '__main__':
    s = "BAAA"
    k = 0
    print(run(s, k))

    s = "AABABBA"
    k = 1
    print(run(s, k))

    s = "ABCD"
    k = 1
    print(run(s, k))

    s = "ABCD"
    k = 0
    print(run(s, k))

    s = "ABBB"
    k = 2
    print(run(s, k))

    s = "BAAAB"
    k = 2
    print(run(s, k))
