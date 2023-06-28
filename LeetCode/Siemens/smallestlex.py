class Solution:
    def nextGreatestLetter(self, letters, target):
        smallest = None

        for char in letters:
            if char > target:
                if not smallest:
                    smallest = char
                else:
                    smallest = min(smallest, char)

        return smallest if smallest else letters[0]


if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = 'c'

    print(Solution().nextGreatestLetter(letters, target))
