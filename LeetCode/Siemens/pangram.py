import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(sentence) == set(string.ascii_lowercase)


if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydo"
    print(Solution().checkIfPangram(sentence))
