import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = math.inf

    def push(self, val: int) -> None:
        self.min = min(val, self.min)
        self.stack.append([val, self.min])

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return -1

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][-1]
        else:
            return -1


if __name__ == '__main__':
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.pop()
    obj.push(-2147483646)
    obj.push(100)
    print(obj.top())
    print(obj.getMin())
