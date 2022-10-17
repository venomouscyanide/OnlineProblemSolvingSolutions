# https://leetcode.com/problems/add-two-numbers/
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


def run(l1, l2):
    # 1 2 3
    # 4 5 6
    digit1 = []
    digit2 = []

    while l1:
        digit1.append(l1.val)
        l1 = l1.next
    while l2:
        digit2.append(l2.val)
        l2 = l2.next

    digit1 = digit1[::-1]
    digit2 = digit2[::-1]

    # if len(digit1) != len(digit2):
    #     if len(digit1) > len(digit2):
    #         digit2.extend([0] * (len(digit1) - len(digit2)))
    #     else:
    #         digit1.extend([0] * (len(digit2) - len(digit1)))

    sum = int("".join(map(lambda x: str(x), digit1))) + int("".join(map(lambda x: str(x), digit2)))

    prev = None
    head = None
    for item in str(sum)[::-1]:
        new_node = ListNode(val=int(item))
        if prev:
            prev.next = new_node
        if not head:
            head = new_node
        prev = new_node

    return head


if __name__ == '__main__':
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    ll1 = create_ll(l1)
    ll2 = create_ll(l2)

    display(run(ll1, ll2))
