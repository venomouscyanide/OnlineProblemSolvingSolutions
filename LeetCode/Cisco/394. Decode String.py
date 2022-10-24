# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        alpha_stack = []
        num_stack = []

        final = ""
        i = 0

        while i < len(s):
            try:
                num = int(s[i])
                if i == 0:
                    num_stack.append(num)
                elif s[i - 1].isdigit():
                    num_stack[-1] = int(str(num_stack[-1]) + s[i])
                else:
                    num_stack.append(num)

                i += 1
                continue
            except:
                pass
            if s[i] == "[":
                if s[i + 1].isdigit():
                    num_stack.append(int(s[i + 1]))
                else:
                    alpha_stack.append(s[i + 1])
                i = i + 2
                continue
            if s[i] == "]":
                num = num_stack.pop()
                alpha = alpha_stack.pop()
                mult = num * alpha

                if len(num_stack) > len(alpha_stack):
                    alpha_stack.append(mult)
                elif len(alpha_stack) != 0:
                    alpha_stack[-1] += mult
                else:
                    final += mult
                i = i + 1
                continue
            else:
                if not alpha_stack:
                    final += s[i]
                else:
                    alpha_stack[-1] += s[i]
                i = i + 1
                continue

        return final


if __name__ == '__main__':
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print(Solution().decodeString(s))

    s = "3[2[z]]"
    print(Solution().decodeString(s))

    s = "3[a5[c]]"
    print(Solution().decodeString(s))

    s = "100[leetcode]"
    print(Solution().decodeString(s))

    s = "33[a]22[c]"
    print(Solution().decodeString(s))

    s = "2[abc]3[cd]ef"
    print(Solution().decodeString(s))

    s = "zzzz2[abc]3[cd]ef"
    print(Solution().decodeString(s))

    s = "1[a]1[b]1[c]de"
    print(Solution().decodeString(s))

    s = "abcde"
    print(Solution().decodeString(s))
