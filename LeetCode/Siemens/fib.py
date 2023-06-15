def fib(n):
    a = 0
    b = 1

    if n == 1:
        return [a]
    if n == 2:
        return [a, b]
    else:
        fib = [a, b]
        for _ in range(2, n):
            c = a + b
            a = b
            b = c
            fib.append(c)
        return fib


def recursive_fib(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)


if __name__ == '__main__':
    print(fib(10))
    print([recursive_fib(n) for n in range(10)])
