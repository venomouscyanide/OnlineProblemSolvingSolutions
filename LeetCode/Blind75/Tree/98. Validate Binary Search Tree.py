# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root) -> bool:
        seq = []
        self.inorder(root, seq)
        print(seq)
        prev = seq[0]
        for item in seq[1:]:
            if item <= prev:
                return False
            prev = item
        return True

    def inorder(self, root, seq):
        if not root:
            return

        self.inorder(root.left, seq)
        seq.append(root.val)
        self.inorder(root.right, seq)
