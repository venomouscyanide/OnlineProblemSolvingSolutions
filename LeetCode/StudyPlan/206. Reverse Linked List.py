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

    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    head = prev
    return head



if __name__ == '__main__':
    list_of_numbers = [1, 2, 4]
    head = create_ll(list_of_numbers)
    display(run(head))
