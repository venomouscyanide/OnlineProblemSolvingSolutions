# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'


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


def run(list1, list2):
    prev = None
    start = None

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            new_head = ListNode(list1.val)
            list1 = list1.next
        else:
            new_head = ListNode(list2.val)
            list2 = list2.next
        if not start:
            start = new_head

        if prev:
            prev.next = new_head
        prev = new_head

    while list1 is not None:
        new_head = ListNode(list1.val)
        if not start:
            start = new_head
        list1 = list1.next
        if prev:
            prev.next = new_head
        prev = new_head

    while list2 is not None:
        new_head = ListNode(list2.val)
        if not start:
            start = new_head
        list2 = list2.next
        if prev:
            prev.next = new_head
        prev = new_head

    return start


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    ll1 = create_ll(list1)
    ll2 = create_ll(list2)

    merged = run(ll1, ll2)
    display(merged)

    list1 = [1000]
    list2 = [1, 1, 2]

    ll1 = create_ll(list1)
    ll2 = create_ll(list2)

    merged = run(ll1, ll2)
    display(merged)
