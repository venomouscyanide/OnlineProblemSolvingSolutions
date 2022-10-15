# https://leetcode.com/problems/merge-k-sorted-lists/
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


def run(lists):
    init = [head for head in lists if head]
    values = [head.val for head in init if head]

    new_new_head = None
    prev = None
    while values:
        min_index = values.index(min(values))
        head_to_increase = init[min_index]

        values[min_index] = head_to_increase.next.val if head_to_increase.next else None
        init[min_index] = head_to_increase.next

        new_head = ListNode(head_to_increase.val)
        if prev:
            prev.next = new_head
        prev = new_head
        if new_new_head is None:
            new_new_head = new_head

        if values[min_index] is None:
            values.pop(min_index)
            init.pop(min_index)

    return new_new_head


if __name__ == '__main__':
    lists = [[0, 2, 5], [1000], [1, 2]]
    new_heads = []

    for val in lists:
        new_heads.append(create_ll(val))

    display(run(new_heads))
