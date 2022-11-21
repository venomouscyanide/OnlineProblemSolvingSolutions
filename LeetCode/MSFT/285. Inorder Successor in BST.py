# https://leetcode.com/problems/inorder-successor-in-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        prev = None
        self.ans = None
        self.next_one = False
        self.inorder(root, prev, p)
        return self.ans

    def inorder(self, root, prev, p):
        if not root or self.ans:
            return

        self.inorder(root.left, prev, p)

        if self.next_one:
            print("Got it")
            self.ans = root
            self.next_one = False
            return

        if root == p:
            self.next_one = True

        self.inorder(root.right, prev, p)
