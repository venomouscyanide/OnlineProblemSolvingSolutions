# https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=level-1

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


def run_ll(list1, list2):
    prev = None
    head = None

    while list1 and list2:
        new_item = ListNode()
        new_item.next = None

        if not head:
            head = new_item

        if list1.val < list2.val:
            new_item.val = list1.val
            list1 = list1.next
        else:
            new_item.val = list2.val
            list2 = list2.next

        if prev:
            prev.next = new_item
            prev = new_item
        else:
            prev = new_item

    while list1:
        new_item = ListNode()

        new_item.next = None
        new_item.val = list1.val

        if not head:
            head = new_item

        if prev:
            prev.next = new_item
            prev = new_item
        else:
            prev = new_item

        list1 = list1.next

    while list2:
        new_item = ListNode()

        if not head:
            head = new_item

        new_item.next = None
        new_item.val = list2.val

        if prev:
            prev.next = new_item
            prev = new_item
        else:
            prev = new_item

        list2 = list2.next

    return head


def display(head):
    print("\n")
    if not head:
        print(head)

    while head:
        print(head.val, end=' ')
        head = head.next


def run(list1, list2):
    new_list = []

    index_l1 = 0
    len_l1 = len(list1)

    index_l2 = 0
    len_l2 = len(list2)

    while index_l1 < len_l1 and index_l2 < len_l2:
        if list1[index_l1] < list2[index_l2]:
            new_list.append(list1[index_l1])
            index_l1 += 1
        else:
            new_list.append(list2[index_l2])
            index_l2 += 1

    while index_l1 < len_l1:
        new_list.append(list1[index_l1])
        index_l1 += 1

    while index_l2 < len_l2:
        new_list.append(list2[index_l2])
        index_l2 += 1

    return new_list


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = []
    head1 = create_ll(list1)
    head2 = create_ll(list2)
    display(run_ll(head1, head2))

    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    head1 = create_ll(list1)
    head2 = create_ll(list2)
    display(run_ll(head1, head2))

    list1 = []
    list2 = [0]
    head1 = create_ll(list1)
    head2 = create_ll(list2)
    display(run_ll(head1, head2))

    list1 = []
    list2 = []
    head1 = create_ll(list1)
    head2 = create_ll(list2)
    display(run_ll(head1, head2))

    list1 = [1, 2, 3]
    list2 = [3, 3, 4, 100]
    head1 = create_ll(list1)
    head2 = create_ll(list2)
    display(run_ll(head1, head2))
