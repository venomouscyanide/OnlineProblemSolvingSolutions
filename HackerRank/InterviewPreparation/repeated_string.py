def repeated_string(string, n):
    total = ((n // len(string)) * string.count('a')) + string[:n % len(string)].count("a")
    return total


if __name__ == '__main__':
    print(repeated_string("a", 1000000000000))
