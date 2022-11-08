# https://leetcode.com/problems/same-tree/
# Attempted in the LC IDE

class Solution:
    def isSameTree(self, p, q) -> bool:
        order_p = []
        order_q = []
        self.preorder(root=p, seq=order_p)
        self.preorder(root=q, seq=order_q)
        # print(order_p)
        # print(order_q)
        return order_p == order_q

    def preorder(self, root, seq):
        seq.append(root.val if root else None)
        if not root:
            return
        self.preorder(root.left, seq)
        self.preorder(root.right, seq)
