# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
import itertools
from itertools import permutations


def run(digits):
    if not digits:
        return []
    letters = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z'],
        0: [' '],
    }

    individual_digits = []
    for digit in digits:
        individual_digits.append(int(digit))

    candidates = []
    for digit in individual_digits:
        candidates.append(letters[digit])

    cart_product = list(itertools.product(*candidates))
    formatted = list(map(lambda x: "".join(x), cart_product))

    return formatted


if __name__ == '__main__':
    digits = ""
    print(run(digits))
