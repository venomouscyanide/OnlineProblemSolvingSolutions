# TODO; optimize, passes all test cases but obv. very slow and impossible to comprehend in its current state
# https://leetcode.com/problems/minimum-window-substring/
from collections import defaultdict, Counter


def run(s, t):
    if len(t) > len(s):
        return ""

    s_counter = Counter()
    t_counter = Counter(t)

    lp = 0
    rp = 0
    longest = s + s

    s_counter[s[rp]] += 1
    while lp <= rp and rp < len(s):
        changed = False
        if len(s_counter.keys()) >= len(t_counter.keys()):
            if set(t_counter.keys()).issubset(set(s_counter.keys())):
                s_counter = {k: v for k, v in sorted(s_counter.items(), key=lambda x: x[0], reverse=True)}
                t_counter = {k: v for k, v in sorted(t_counter.items(), key=lambda x: x[0], reverse=True)}

                subset = True
                for key, value in t_counter.items():
                    if s_counter[key] - value < 0:
                        subset = False
                        break
                s_counter = Counter(s_counter)
                t_counter = Counter(t_counter)

                if subset and len(longest) > len(s[lp:rp + 1]):
                    changed = True
                    longest = s[lp:rp + 1]
                    s_counter[s[lp]] -= 1
                    if not s_counter[s[lp]]:
                        del s_counter[s[lp]]
                    lp += 1
                    if lp > rp and lp < len(s):
                        rp = lp
                        s_counter[s[rp]] += 1

                lp_inc = True
                for key, value in t_counter.items():
                    if s_counter[key] < value:
                        lp_inc = False

                if lp_inc and not changed:
                    changed = True
                    s_counter[s[lp]] -= 1
                    if not s_counter[s[lp]]:
                        del s_counter[s[lp]]
                    lp += 1

        if not changed:
            if rp == len(s) - 1:
                s_counter[s[lp]] -= 1
                if not s_counter[s[lp]]:
                    del s_counter[s[lp]]
                lp += 1
            if rp + 1 < len(s):
                rp = rp + 1
                s_counter[s[rp]] += 1

    if longest == s + s:
        longest = ""
    return longest


if __name__ == '__main__':
    s = "cabefgecdaecf"
    t = "cae"
    print(run(s, t))

    s = "acbbaca"
    t = "aba"
    print(run(s, t))

    s = "bbaa"
    t = "aba"
    print(run(s, t))

    s = "aa"
    t = "aa"
    print(run(s, t))

    s = "abc"
    t = "cba"
    print(run(s, t))

    s = "abbbbbcdd"
    t = "abcdd"
    print(run(s, t))

    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"
    print(run(s, t))

    s = "abc"
    t = "cba"
    print(run(s, t))

    s = "ADOBECODEBANC"
    t = "ABC"
    print(run(s, t))

    s = "ab"
    t = "a"
    print(run(s, t))

    s = "ab"
    t = "b"
    print(run(s, t))

    s = "ab"
    t = "z"
    print(run(s, t))
