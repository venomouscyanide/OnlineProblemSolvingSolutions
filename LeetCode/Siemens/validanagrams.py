from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        check = len(p)

        set_p = Counter(p)
        slices = [Counter(s[i:i + check]) for i in range(0, len(s) - check + 1, 1)]

        output = []

        for index, slice in enumerate(slices):
            if slice == set_p:
                output.append(index)

        return output


if __name__ == '__main__':
    s = "ababababab"
    p = "aab"
    print(Solution().findAnagrams(s, p))

    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))

    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s, p))
