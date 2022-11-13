# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        preorder_seq = []

        self.preorder(root, preorder_seq)

        delim = "%%%"
        inorder_str = delim.join(preorder_seq)
        # print(preorder_seq)
        return inorder_str

    def preorder(self, root, seq):
        if not root:
            seq.append("N")
            return
        seq.append(str(root.val))
        self.preorder(root.left, seq)
        self.preorder(root.right, seq)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        delim = "%%%"

        preorder = data.split(delim)
        # print(preorder)

        root = self.reconstruct(preorder)
        return root

    def reconstruct(self, preorder):
        if preorder:
            root_val = preorder.pop(0)

            if root_val == "N":
                return
            else:
                root = TreeNode(int(root_val))
                # print(root_val, preorder)
                root.left = self.reconstruct(preorder)
                root.right = self.reconstruct(preorder)
                return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
