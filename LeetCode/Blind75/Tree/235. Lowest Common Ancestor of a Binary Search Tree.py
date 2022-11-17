# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca_node = self.lca(root, p, q)
        return lca_node

    def lca(self, root, p, q):
        if not root:
            return

        if p.val < root.val and q.val < root.val:
            return self.lca(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lca(root.right, p, q)
        else:
            return root
