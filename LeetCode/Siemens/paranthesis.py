class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close_mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        open = set(open_close_mapping.values())

        valid = True
        for char in s:
            if char in open:
                stack.append(char)
            else:
                if not stack:
                    valid = False
                    break
                elif open_close_mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    valid = False
                    break
        if stack:
            valid = False
        return valid


if __name__ == '__main__':
    s = "(())"
    print(Solution().isValid(s))
