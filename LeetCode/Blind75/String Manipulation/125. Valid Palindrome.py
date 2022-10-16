# https://leetcode.com/problems/valid-palindrome/


def run(s):
    s = s.lower()
    s = filter(lambda x: x.isalnum(), s)
    s = "".join(s)
    return s == s[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(run(s))

    s = "race a car"
    print(run(s))
