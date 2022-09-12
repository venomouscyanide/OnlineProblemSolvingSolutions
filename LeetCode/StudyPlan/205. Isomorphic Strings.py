# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1
from collections import defaultdict


def run(s, t):
    if len(s) != len(t):
        return False

    if s == t:
        return True

    def check_l_r(s, t):
        check = defaultdict(int)
        check_s = [0 for _ in range(len(s))]
        check_t = [0 for _ in range(len(s))]

        for index, char in enumerate(s):
            check_s[index] = ord(char)
            check_t[index] = ord(t[index])

        fail = True

        for index, ascii_id in enumerate(check_s):
            if not check[ascii_id]:
                check[ascii_id] = check_t[index]
            else:
                fail = check[ascii_id] == check_t[index]
                if not fail:
                    break
        return fail

    left = check_l_r(s, t)
    right = check_l_r(t, s)

    return all([left, right])


if __name__ == '__main__':
    s = "aaaaa"
    t = "aaaaa"
    print(run(s, t))

    s = "turtle"
    t = "tletur"
    print(run(s, t))

    s = "bbbaaaba"
    t = "aaabbbba"
    print(run(s, t))

    s = "badc"
    t = "baba"
    print(run(s, t))

    s = 'foo'
    t = 'bar'
    print(run(s, t))

    s = "egg"
    t = "add"
    print(run(s, t))

    s = "paper"
    t = "title"
    print(run(s, t))
