# https://leetcode.com/problems/longest-palindromic-substring/
# with help from: https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).

def run(s):
    # expand around the centre approach

    def __palindrome_around_center(string, left, right):
        tot = len(string)

        while left >= 0 and right < tot and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1: right]

    longest = ""

    for index in range(len(s)):
        palindrome = __palindrome_around_center(s, index, index)
        longest = palindrome if len(palindrome) > len(longest) else longest

        palindrome = __palindrome_around_center(s, index, index + 1)
        longest = palindrome if len(palindrome) > len(longest) else longest

    return longest


if __name__ == '__main__':
    s = "caba"
    print(run(s))

    s = "abbb"
    print(run(s))

    s = "aba"
    print(run(s))

    s = "babad"
    print(run(s))

    s = "abcddcba"
    print(run(s))

    s = "cbbd"
    print(run(s))

    s = "abpollllopcbbdqwertyytrewq"
    print(run(s))

    s = "aaaaaaaab"
    print(run(s))
