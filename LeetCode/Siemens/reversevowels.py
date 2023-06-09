class Solution:
    def reverseVowels(self, s: str) -> str:
        indices = set()
        vowels_encountered = []

        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        for index, char in enumerate(s):
            if char in vowels:
                indices.add(index)
                vowels_encountered.append(char)

        updated_str = []

        for index, char in enumerate(s):
            if index in indices:
                updated_str.append(vowels_encountered.pop())
            else:
                updated_str.append(char)

        return "".join(updated_str)


if __name__ == '__main__':
    s = "leetcode"
    print(Solution().reverseVowels(s))
