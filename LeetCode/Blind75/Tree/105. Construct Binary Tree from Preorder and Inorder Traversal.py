# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional['TreeNode']:
        new_root = self.build_tree_helper(preorder, inorder)
        return new_root

    def build_tree_helper(self, preorder, inorder):
        root = self.build_tree(preorder, inorder)
        return root

    def build_tree(self, preorder, inorder):
        if inorder:
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            # print(root_val, preorder, inorder)
            root.left = self.build_tree(preorder, inorder[0:inorder.index(root_val)])
            root.right = self.build_tree(preorder, inorder[inorder.index(root_val) + 1:])
            return root
