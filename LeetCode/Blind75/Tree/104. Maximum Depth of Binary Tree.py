# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Attempted in the LC IDE
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left) if root.left else 0
        right = self.maxDepth(root.right) if root.right else 0

        max_depth = 1 + max(left, right)

        return max_depth
