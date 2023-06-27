class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = len(nums1) - 1
        j = m - 1
        k = len(nums2) - 1

        check_nums1 = True
        check_nums2 = True
        if m == 0:
            check_nums1 = False
        if n == 0:
            check_nums2 = False

        while i >= 0 and nums2:
            if nums1[j] >= nums2[k] and check_nums1:
                nums1[i] = nums1[j]
                if j == 0:
                    check_nums1 = False
                else:
                    j -= 1
            elif check_nums2:
                nums1[i] = nums2[k]

                if k == 0:
                    check_nums2 = False
                else:
                    k -= 1
            else:
                break
            i -= 1

        return nums1


if __name__ == '__main__':
    nums1 = [0, 0, 0, 0, 0, 0]
    m = 0
    nums2 = [1, 2, 3, 4, 5, 6]
    n = 6
    print(Solution().merge(nums1, m, nums2, n))

    nums1 = [5, 5, 11, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    print(Solution().merge(nums1, m, nums2, n))

    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    print(Solution().merge(nums1, m, nums2, n))

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(Solution().merge(nums1, m, nums2, n))

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(Solution().merge(nums1, m, nums2, n))
