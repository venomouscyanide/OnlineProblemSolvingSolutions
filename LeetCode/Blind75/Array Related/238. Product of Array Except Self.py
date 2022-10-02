# https://leetcode.com/problems/product-of-array-except-self/
def run(nums):
    left = [1 for _ in range(len(nums))]
    right = [1 for _ in range(len(nums))]

    counter = 1
    for num in nums[0:-1]:
        left[counter] = num * left[counter - 1]
        counter += 1

    counter = 1
    for num in nums[::-1][:-1]:
        right[counter] = num * right[counter - 1]
        counter += 1

    final = []
    for i, j in zip(left, right[::-1]):
        final.append(i * j)

    return final


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    run(nums)
