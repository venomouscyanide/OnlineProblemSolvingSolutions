# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def run(strs):
    grouped_anagrams = defaultdict(list)

    for str in strs:
        sorted_str = ''.join(sorted(str))
        grouped_anagrams[sorted_str].append(str)

    return list(grouped_anagrams.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(run(strs))
