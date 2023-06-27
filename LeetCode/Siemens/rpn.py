def do_operation(a, b, token):
    a = int(a)
    b = int(b)
    if token == "+":
        return a + b
    elif token == "-":
        return a - b
    elif token == "/":
        return int(a / b)
    else:
        return a * b


class Solution:
    def evalRPN(self, tokens):
        operands = {'*', '/', '+', '-'}

        while len(tokens) > 1:
            for index, token in enumerate(tokens):
                if token in operands:
                    a = tokens[index - 2]
                    b = tokens[index - 1]
                    c = do_operation(a, b, token)
                    tokens[index] = c
                    tokens.pop(index - 1)
                    tokens.pop(index - 2)
                    break

        return int(tokens[0])


if __name__ == '__main__':
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))

    tokens = ["4", "13", "5", "/", "+"]
    print(Solution().evalRPN(tokens))

    tokens = ["4"]
    print(Solution().evalRPN(tokens))
