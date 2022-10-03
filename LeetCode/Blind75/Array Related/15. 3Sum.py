# https://leetcode.com/problems/3sum/

def run(nums):
    nums.sort()
    tot = len(nums)
    chosen = set()
    final_list = []

    for index in range(0, tot - 2, 1):
        lp = index + 1
        rp = tot - 1

        while lp < rp:
            to_add = (nums[lp], nums[rp], nums[index])

            if to_add in chosen:
                lp += 1
                rp -= 1
                continue

            if nums[lp] + nums[rp] + nums[index] > 0:
                rp -= 1
            elif nums[lp] + nums[rp] + nums[index] < 0:
                lp += 1
            else:
                chosen.add(to_add)
                final_list.append([to_add[0], to_add[1], to_add[2]])
                lp += 1
                rp -= 1

    return final_list


if __name__ == '__main__':
    nums = [3, 0, -2, -1, 1, 2]
    print(run(nums))

    nums = [-2, 0, 1, 1, 2]
    print(run(nums))

    nums = [0, 0, 0, 0]
    print(run(nums))

    nums = [-1, 0, 1, 2, -1, -4]
    print(run(nums))

    nums = [0, 1, 1]
    print(run(nums))

    nums = [0, 0, 0]
    print(run(nums))
