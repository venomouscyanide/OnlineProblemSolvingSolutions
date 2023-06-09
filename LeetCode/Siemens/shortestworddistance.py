import math


class Solution:
    def shortestDistance(self, wordsDict, word1, word2):
        min_distance = math.inf
        index1 = index2 = -1

        for index, word in enumerate(wordsDict):
            if word == word1:
                index1 = index
            if word == word2:
                index2 = index

            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index2 - index1))

        return min_distance


if __name__ == '__main__':
    wordsDict = ["a", "c", "a", "b"]
    word1 = "a"
    word2 = "b"
    print(Solution().shortestDistance(wordsDict, word1, word2))

    wordsDict = ["a", "b", "d", "d"]
    word1 = "a"
    word2 = "d"
    print(Solution().shortestDistance(wordsDict, word1, word2))

    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "coding"
    print(Solution().shortestDistance(wordsDict, word1, word2))
