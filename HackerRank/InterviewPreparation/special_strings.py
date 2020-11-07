"""
https://www.hackerrank.com/challenges/special-palindrome-again/submissions/code/186718642
This solution gets timed out :(
"""
import itertools


def number_of_special_strings(n, string):
    tot = 0
    string_list = list(string)

    for i, j in itertools.combinations(range(n + 1), 2):
        sub_list = string_list[i:j]
        sub_set = set(sub_list)
        org_len = j - i
        sub_len = len(sub_set)
        if sub_len == 1:
            tot += 1
        elif sub_len == 2 and org_len % 2 != 0:
            sub_list.pop(org_len // 2)
            consider = len(set(sub_list)) == 1
            if consider:
                tot += 1
    return tot


if __name__ == '__main__':
    print(number_of_special_strings(5, 'abcde'))
