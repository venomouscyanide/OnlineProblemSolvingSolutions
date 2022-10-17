# https://leetcode.com/problems/count-and-say/
from collections import Counter, defaultdict

map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

reverse_map = {v: k for k, v in map.items()}


def run(n):
    original_n = n
    n = str(1)

    for _ in range(original_n - 1):
        count = defaultdict(int)
        prev = n[0]

        sayings = []
        count[prev] += 1
        for item in n[1:]:
            if item == prev:
                count[item] += 1
            else:
                sayings.append(f"{reverse_map[count[prev]]},{reverse_map[int(prev)]}")
                prev = item
                count[item] = 1
                count[prev] = 1
        if len(n) == 1:
            sayings.append("one,one")
        else:
            sayings.append(f"{reverse_map[count[item]]},{reverse_map[int(item)]}")


        back_to_int = []
        for saying in sayings:
            saying = saying.split(',')
            for say in saying:
                back_to_int.append(str(map[say]))
        n = "".join(back_to_int)
    n = str(n)
    return n


if __name__ == '__main__':
    print(run(1))

    # print(run(2))
    #
    # print(run(3))
    #
    # print(run(4))
    #
    # print(run(5))
