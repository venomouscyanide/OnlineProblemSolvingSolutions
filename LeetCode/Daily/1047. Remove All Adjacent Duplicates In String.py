# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        stack.append(s[0])

        for char in s[1:]:
            if stack:
                last_item = stack[-1]
                if char == last_item:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)
