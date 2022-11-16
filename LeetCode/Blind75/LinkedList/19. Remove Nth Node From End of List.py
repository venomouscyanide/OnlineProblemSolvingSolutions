# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __repr__(self):
    #     return f'{self.val}, {self.next}'


def create_ll(list_of_numbers):
    prev = None
    head = None

    for index, item in enumerate(list_of_numbers):
        new_item = ListNode()
        new_item.next = None

        if not head:
            head = new_item

        new_item.val = item
        if prev:
            prev.next = new_item
            prev = new_item
        else:
            prev = new_item

    return head


def display(head):
    print("\n")
    if not head:
        print(head)

    while head:
        print(head.val, end=' ')
        head = head.next


class Solution:
    def removeNthFromEnd(self, head, n):
        root = head
        node = head

        list_of_nums = []
        while node:
            list_of_nums.append(node)
            node = node.next
        if n + 1 <= len(list_of_nums):
            node = list_of_nums[-n - 1]
            node.next = node.next.next
        else:
            root = root.next
        return root


if __name__ == '__main__':
    list_of_numbers = [1]
    head = create_ll(list_of_numbers)
    display(head)
    new_head = Solution().removeNthFromEnd(head, 1)
    display(new_head)
