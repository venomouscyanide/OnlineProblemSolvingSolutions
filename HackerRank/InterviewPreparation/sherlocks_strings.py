"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
"""
from collections import defaultdict, Counter
from pprint import pprint


def sherlocks_string(string):
    element_count = defaultdict(int)
    for element in string:
        element_count[element] += 1
    # pprint(dict(element_count))
    count_values = list(element_count.values())
    counter = Counter(count_values)
    most_common = counter.most_common()
    # pprint(most_common)
    if len(most_common) > 2:
        return "NO"
    if len(most_common) == 1:
        return "YES"

    first_element_len, first_element_count = most_common[0]
    second_element_len, second_element_count = most_common[1]
    if second_element_len == 1 and second_element_count == 1:
        return "YES"
    elif abs(first_element_len - second_element_len) == 1 and second_element_count == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    print(sherlocks_string('aaaabbcc'))
