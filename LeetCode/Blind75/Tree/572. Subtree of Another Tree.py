# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        inorder_a = ['']
        self.preorder(root, inorder_a)
        inorder_b = ['']
        self.preorder(subRoot, inorder_b)
        len_b = len(inorder_b)
        # print(inorder_a, inorder_b)

        inorder_a = "".join(inorder_a)
        inorder_b = "".join(inorder_b)
        # print(inorder_a)
        # print(inorder_b)
        found = inorder_b in inorder_a
        # print(found)
        return found

    def preorder(self, root, seq):
        if not root:
            seq.append("#")
            return
        seq.append(f"~{root.val}")
        self.preorder(root.left, seq)
        self.preorder(root.right, seq)

