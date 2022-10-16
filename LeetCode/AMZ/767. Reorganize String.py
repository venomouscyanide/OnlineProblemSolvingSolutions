# https://leetcode.com/problems/reorganize-string/
from collections import Counter


def run(str):
    counter = Counter(str)
    new_str = ""
    sorted_occ = {k: v for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=False)}

    prev = ""
    while any(sorted_occ.values()):
        for letter in sorted_occ.keys():
            if not sorted_occ[letter]:
                continue
            if prev == letter:
                return ""
            prev = letter
            sorted_occ[letter] -= 1
            new_str += letter
    return new_str


if __name__ == '__main__':
    s = "vvvlo"
    print(run(s))
