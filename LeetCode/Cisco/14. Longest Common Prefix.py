# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[-1]

        prefix = ""
        prev = strs[0]

        for a, b in zip(prev, strs[1]):
            if a == b:
                prefix += a
            else:
                break

        for str in strs[2:]:
            if not str:
                return ""

            if not prefix:
                break

            zipped_str = zip(str, prefix)

            for index, (a, b) in enumerate(zipped_str):
                if a == b:
                    if index >= len(prefix):
                        prefix += a
                else:
                    prefix = prefix[:index]
                    break
            if len(str) < len(prefix):
                prefix = str

        return prefix


if __name__ == '__main__':
    strs = ["flower", "flow", "fl", 'floww', 'f']
    print(Solution().longestCommonPrefix(strs))

    strs = ["reflower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))

    strs = ["carr", "carr", "carr11", "carr"]
    print(Solution().longestCommonPrefix(strs))

    strs = ["abab", "aba", ""]
    print(Solution().longestCommonPrefix(strs))

    strs = ["abab",  ""]
    print(Solution().longestCommonPrefix(strs))

    strs = [""]
    print(Solution().longestCommonPrefix(strs))

    strs = ["ac", "ac", "a", "a"]
    print(Solution().longestCommonPrefix(strs))
