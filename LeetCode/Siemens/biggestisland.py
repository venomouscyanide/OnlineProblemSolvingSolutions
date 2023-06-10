from pprint import pprint


def maxAreaIslandDFS(matrix):
    num_cols = len(matrix[0])
    num_rows = len(matrix)

    max_count = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 1:
                count = 0
                current_count = dfs(matrix, i, j, num_rows, num_cols, count)
                max_count = max(current_count, max_count)

    return max_count


def dfs(matrix, i, j, num_rows, num_cols, count):
    matrix[i][j] = 0
    count += 1

    for coordinate in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i = i + coordinate[0]
        new_j = j + coordinate[-1]

        if new_i >= num_rows or new_i < 0 or new_j >= num_cols or new_j < 0:
            continue
        elif matrix[new_i][new_j] == 0:
            continue
        else:
            count = dfs(matrix, new_i, new_j, num_rows, num_cols, count)
    return count


def main():
    # pprint([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
    #     0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]])
    print(maxAreaIslandDFS([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
    # print(maxAreaIslandDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]))


if __name__ == '__main__':
    main()
