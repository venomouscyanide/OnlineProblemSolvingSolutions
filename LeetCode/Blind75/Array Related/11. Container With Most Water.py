# https://leetcode.com/problems/container-with-most-water/

def run(height):
    if not height:
        return

    if len(height) == 2:
        return min(height) * min(height)

    lp = 0
    rp = len(height) - 1

    max_storage = 0

    while lp < rp:
        minimum = min(height[lp], height[rp])
        max_storage = max(max_storage, minimum * (rp - lp))

        if height[lp] >= height[rp]:
            rp -= 1
        else:
            lp += 1

    return max_storage


if __name__ == '__main__':
    height = [2, 3, 4, 5, 18, 17, 6]
    print(run(height))

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(run(height))

    height = [1, 1]
    print(run(height))

    height = [1, 1, 2, 2, 2, 4, 5]
    print(run(height))
