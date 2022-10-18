# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
def run(s, k):
    stack_count = []

    prev = s[0]
    stack_count.append([prev, 1])

    new_s = [s[0]]
    for item in s[1:]:
        new_s.append(item)
        if prev == item:
            stack_count[-1][-1] += 1
        else:
            stack_count.append([item, 1])

        if stack_count[-1][-1] == k:
            del new_s[len(new_s) - k:]
            stack_count.pop()
            prev = stack_count[-1][0] if stack_count else ""
        else:
            prev = stack_count[-1][0]
    return "".join(new_s)


if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    print(run(s, k))

    s = "abcd"
    k = 2
    print(run(s, k))

    s = "abbad"
    k = 2
    print(run(s, k))
