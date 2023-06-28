class Solution:
    def strStr(self, haystack: str, needle: str):
        len_needle = len(needle)

        slices = [haystack[i: i + len_needle] for i in range(0, len(haystack) - len(needle) + 1)]

        for index, slice in enumerate(slices):
            if slice == needle:
                return index

        return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    print(Solution().strStr(haystack, needle))

    haystack = "leetcode"
    needle = "co"
    print(Solution().strStr(haystack, needle))
