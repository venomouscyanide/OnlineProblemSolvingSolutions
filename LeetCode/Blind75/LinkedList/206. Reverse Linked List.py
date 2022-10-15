# this is a re-do as it comes up in blind75
# https://leetcode.com/problems/reverse-linked-list/?envType=study-plan&id=level-1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'


def create_ll(list_of_numbers):
    prev = None
    head = None

    for item in list_of_numbers:
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


def run(head):
    current = head
    prev = None

    if not current:
        return current

    while current.next:
        next = current.next
        current.next = prev
        prev = current
        current = next
    current.next = prev
    return current


if __name__ == '__main__':
    list_of_numbers = []
    head = create_ll(list_of_numbers)
    display(run(head))

    list_of_numbers = [1, 2, 4]
    head = create_ll(list_of_numbers)
    display(run(head))

    list_of_numbers = [1, 2, 3, 4, 5, 6]
    head = create_ll(list_of_numbers)
    display(run(head))

    list_of_numbers = [1, 1]
    head = create_ll(list_of_numbers)
    display(run(head))

    list_of_numbers = [1]
    head = create_ll(list_of_numbers)
    display(run(head))
