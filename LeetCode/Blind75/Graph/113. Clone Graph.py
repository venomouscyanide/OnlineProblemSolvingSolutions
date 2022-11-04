# https://leetcode.com/problems/clone-graph/
# solution coded in Leetcode, hence the missing classes bug below
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        node_copy = Node(val=node.val, neighbors=None)

        stack = [node_copy]
        seen = set()
        seen.add(node_copy.val)

        neigh_map = defaultdict(list)
        neigh_map[node_copy.val] = node.neighbors
        new_obj_map = {
            node_copy.val: node_copy
        }
        initial_seen = 1

        while len(stack) >= 1:
            print("len", len(stack))
            if stack:
                for i in stack:
                    print(i.val, end=', ')
            print("", seen)
            current_node = stack.pop(-1)

            if current_node.val not in seen:
                current_node = new_obj_map[current_node.val]
                seen.add(current_node.val)
            elif not initial_seen:
                continue
            initial_seen = 0

            neighbors = neigh_map[current_node.val]

            total_copies = []
            for neighbor in neighbors:
                obj_copy = new_obj_map.get(neighbor.val)
                if not obj_copy:
                    obj_copy = Node(val=neighbor.val, neighbors=None)
                    new_obj_map[obj_copy.val] = obj_copy
                total_copies.append(obj_copy)
                neigh_map[obj_copy.val] = neighbor.neighbors
                if obj_copy.val not in seen:
                    stack.append(obj_copy)

            for copy in total_copies:
                current_node.neighbors.append(copy)

        return node_copy
