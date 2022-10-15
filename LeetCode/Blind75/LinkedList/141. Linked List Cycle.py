# https://leetcode.com/problems/linked-list-cycle/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __repr__(self):
    #     return f'{self.val}, {self.next}'


def create_ll(list_of_numbers, pos):
    prev = None
    head = None
    cycle = None
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

        if index == pos:
            cycle = new_item

    if pos != -1:
        new_item.next = cycle

    return head


def display(head):
    print("\n")
    if not head:
        print(head)

    while head:
        print(head.val, end=' ')
        head = head.next


def run(head) -> bool:
    # inf loop currently
    seen = set()

    current = head
    fp = current

    if not current:
        return False

    while current.next:
        if fp.next == current:
            return True
        else:
            if fp.next is None or fp in seen:
                current = current.next
            else:
                seen.add(fp)
                fp = fp.next
    return False


if __name__ == '__main__':
    list_of_numbers = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21,
                       23, -21, 5]
    pos = -1
    head = create_ll(list_of_numbers, pos=-1)
    print(run(head))

    list_of_numbers = [1, 2, 1]
    pos = 1
    head = create_ll(list_of_numbers, pos)
    print(run(head))

    list_of_numbers = [1, 2, 1]
    head = create_ll(list_of_numbers, pos=0)
    print(run(head))

    list_of_numbers = [1, 2, 1]
    head = create_ll(list_of_numbers, pos=2)
    print(run(head))
