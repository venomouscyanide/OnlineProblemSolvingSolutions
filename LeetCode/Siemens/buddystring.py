from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        changes = []

        if len(s) != len(goal):
            return False

        for index, (char1, char2) in enumerate(zip(s, goal)):
            if char1 != char2:
                changes.append(index)

        if len(changes) == 2:
            s = list(s)
            s[changes[0]], s[changes[1]] = s[changes[1]], s[changes[0]]
            return "".join(s) == goal
        elif Counter(s).most_common(1)[0][-1] >= 2 and Counter(goal).most_common(1)[0][-1] >= 2:
            if not changes:
                return True
            else:
                if len(changes) == 1:
                    s = list(s)
                    s[changes[0]], s[changes[0] - 1] = s[changes[0] - 1], s[changes[0]]
                    return "".join(s) == goal
                else:
                    return False
        else:
            return False


if __name__ == '__main__':
    s = "ab"
    goal = "ba"
    print(Solution().buddyStrings(s, goal))

    s = "ab"
    goal = "ab"
    print(Solution().buddyStrings(s, goal))

    s = "aaa"
    goal = "aaa"
    print(Solution().buddyStrings(s, goal))

    s = "ana"
    goal = "aba"
    print(Solution().buddyStrings(s, goal))

    s = "aba"
    goal = "aab"
    print(Solution().buddyStrings(s, goal))
