# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import defaultdict
from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return

        level_dict = defaultdict(list)
        level_dict[0].append(root.val)
        self.dfs(root, level_dict, level=1)
        # print(level_dict)
        level_order = list(filter(lambda x: len(x) > 0, level_dict.values()))
        return level_order

    def dfs(self, root, level_dict, level):
        if not root:
            return
        left = root.left.val if root.left else None
        right = root.right.val if root.right else None
        to_add = [left, right]
        to_add = list(filter(lambda x: x is not None, to_add))
        level_dict[level].extend(to_add)
        if not to_add:
            return
        self.dfs(root.left, level_dict, level + 1)
        self.dfs(root.right, level_dict, level + 1)
