# https://leetcode.com/problems/reverse-integer/submissions/g
def run(x):
    prepend = False

    if x < 0:
        prepend = True
        xs = str(x)
        xs = xs[1:]
    else:
        xs = str(x)

    xs = xs[::-1]
    xs = int(xs)
    if prepend:
        xs = -xs

    if not (xs < 2 ** 31 - 1 and xs > -2 ** 31):
        return 0

    return xs


if __name__ == '__main__':
    print(run(1534236469))
    print(run(-1123))
