# https://leetcode.com/problems/valid-anagram/


def run(s, t):
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(run(s, t))

    s = "rat"
    t = "car"
    print(run(s, t))
