# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image, sr, sc, color):
        self.max_row = len(image)
        self.max_col = len(image[0])
        old = image[sr][sc]
        if old == color:
            return image

        self.recursive(image, sr, sc, old, color)
        return image

    def recursive(self, image, row, col, old, new):
        if row < 0 or row >= self.max_row or col < 0 or col >= self.max_col:
            return

        if image[row][col] == old:
            image[row][col] = new

            self.recursive(image, row + 1, col, old, new)
            self.recursive(image, row - 1, col, old, new)
            self.recursive(image, row, col + 1, old, new)
            self.recursive(image, row, col - 1, old, new)
        return
