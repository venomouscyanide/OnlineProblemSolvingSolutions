from pprint import pprint


def floodFill(matrix, x, y, new_color):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    original_color = matrix[x][y]
    dfs(matrix, x, y, original_color, num_rows, num_cols, new_color)

    return matrix


def dfs(matrix, i, j, original_color, num_rows, num_cols, new_color):
    matrix[i][j] = new_color

    for coordinate in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i = i + coordinate[0]
        new_j = j + coordinate[1]

        if new_j < 0 or new_j >= num_cols or new_i < 0 or new_i >= num_rows:
            continue
        elif matrix[new_i][new_j] != original_color:
            continue
        else:
            dfs(matrix, new_i, new_j, original_color, num_rows, num_cols, new_color)


def main():
    pprint([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]])
    pprint(floodFill([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]], 1, 3, 2))

    pprint([[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])
    pprint(floodFill([[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], 3, 2, 5))


if __name__ == '__main__':
    main()
