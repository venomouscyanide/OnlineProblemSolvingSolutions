# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional['TreeNode'], k: int) -> int:
        n = 0
        self.k = k
        self.ans = None
        seq = []
        self.preorder(root, seq)
        return self.ans

    def preorder(self, root, seq):
        if not root:
            return

        if self.ans:
            return

        self.preorder(root.left, seq)

        seq.append(root.val)
        if self.k == len(seq):
            self.ans = seq[-1]
            return

        self.preorder(root.right, seq)
