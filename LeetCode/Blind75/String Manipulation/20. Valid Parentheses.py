# https://leetcode.com/problems/valid-parentheses/

def run(s):
    stack = []
    open_close_mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    open = set(open_close_mapping.values())

    for char in s:
        if char in open:
            stack.append(char)
            continue
        if not stack:
            return False
        last_char = stack[-1]
        if last_char == open_close_mapping[char]:
            stack.pop()
        else:
            return False
    if not stack:
        return True
    return False


if __name__ == '__main__':
    s = "]"
    print(run(s))

    s = "("
    print(run(s))

    s = "()"
    print(run(s))

    s = "({{[]}})"
    print(run(s))

    s = "({{[)]}})"
    print(run(s))
