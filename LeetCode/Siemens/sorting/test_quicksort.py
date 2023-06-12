import unittest

from LeetCode.Siemens.sorting.quick_sort import quick_sort_helper


class TestQuickSort(unittest.TestCase):
    def test_desc_quick_sort(self):
        original_list = [5, 3, 1, 5]
        copy_list = original_list.copy()
        quick_sort_helper(copy_list, first=0, last=len(copy_list) - 1)
        self.assertListEqual(copy_list, sorted(original_list, reverse=True), "Quicksort logic failed")


if __name__ == '__main__':
    unittest.main()
