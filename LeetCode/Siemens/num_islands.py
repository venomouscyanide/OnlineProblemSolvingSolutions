from pprint import pprint


def countIslandsDFS(matrix):
    total_islands = 0
    num_cols = len(matrix[0])
    num_rows = len(matrix)

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 1:
                dfs(i, j, matrix, num_rows, num_cols)
                total_islands += 1

    return total_islands


def dfs(i, j, matrix, num_rows, num_cols):
    matrix[i][j] = 0

    for coordinates in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i = i + coordinates[0]
        new_j = j + coordinates[-1]
        if not (new_i < num_cols and new_i >= 0 and new_j < num_rows and new_j >= 0):
            continue
        elif matrix[new_i][new_j] == 0:
            continue
        else:
            dfs(new_i, new_j, matrix, num_rows, num_cols)


def main():
    pprint([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]])
    pprint([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])
    print(countIslandsDFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(countIslandsDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))


if __name__ == '__main__':
    main()
