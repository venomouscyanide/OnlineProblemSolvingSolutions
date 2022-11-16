# https://leetcode.com/problems/reorder-list/
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
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return head

        node = head
        list_of_nodes = []

        while node:
            list_of_nodes.append(node)
            node = node.next

        i = 0
        j = len(list_of_nodes) - 1

        prev = None
        while i < j:
            if prev:
                prev.next = list_of_nodes[i]
            list_of_nodes[i].next = list_of_nodes[j]
            prev = list_of_nodes[j]

            i += 1
            j -= 1
        if len(list_of_nodes) % 2 == 0:
            prev.next = None
        else:
            list_of_nodes[len(list_of_nodes) // 2].next = None
            prev.next = list_of_nodes[len(list_of_nodes) // 2]


if __name__ == '__main__':
    list_of_numbers = [1, 2, 3, 4, 6, 7]
    head = create_ll(list_of_numbers)
    display(head)
    Solution().reorderList(head)
    display(head)
