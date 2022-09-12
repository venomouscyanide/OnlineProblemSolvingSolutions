# https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1


def run(s, t):
    if not len(s) and len(t):
        return True

    if not s and not t:
        return True

    if len(t) < len(s):
        return False

    for index, char in enumerate(t):
        if s[0] == char:
            s = s[1:]

        if not s:
            break

    if not s:
        return True
    else:
        return False


if __name__ == '__main__':
    s = 'abc'
    t = 'ahbgdc'
    print(run(s, t))

    s = 'axc'
    t = 'ahbgdc'
    print(run(s, t))

    s = ''
    t = 'ahbgdc'
    print(run(s, t))

    s = 'axc'
    t = ''
    print(run(s, t))

    s = ''
    t = ''
    print(run(s, t))