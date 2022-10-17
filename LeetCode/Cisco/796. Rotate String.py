# https://leetcode.com/problems/rotate-string/

def run(s, goal):
    tot = len(s)
    for index in range(0, tot):
        new_part_1 = s[1:]
        new_part_2 = s[: 1]
        s = new_part_1 + new_part_2
        print(s)
        if s == goal:
            return True

    return False


if __name__ == '__main__':
    s = "abcde"
    goal = "cdeab"
    print(run(s, goal))
