# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head):
        int_vals = ""
        while head:
            val = head.val
            head = head.next
            int_vals += str(val)

        return int(int_vals, 2)
