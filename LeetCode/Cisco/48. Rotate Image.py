# https://leetcode.com/problems/rotate-image/

def run(matrix):
    n = len(matrix)

    # swaps along y
    top_down = n - 1
    for i in range(0, n // 2, 1):
        matrix[i], matrix[top_down] = matrix[top_down], matrix[i]
        top_down -= 1

    # transpose
    for i in range(0, n, 1):
       for j in range(i+1, n, 1):
           matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    run(matrix)
    print(matrix)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    run(matrix)
    print(matrix)
