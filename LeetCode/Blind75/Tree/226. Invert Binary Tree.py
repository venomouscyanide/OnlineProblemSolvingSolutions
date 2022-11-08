# https://leetcode.com/problems/invert-binary-tree/
# Completed in LC IDE

class Solution:
    def invertTree(self, root):
        if not root:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root
