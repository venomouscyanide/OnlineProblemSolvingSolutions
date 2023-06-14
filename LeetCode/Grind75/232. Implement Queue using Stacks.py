class MyQueue:
    def __init__(self):
        self.stack1 = MyStack()
        self.stack2 = MyStack()

    def push(self, x: int) -> None:
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(x)
        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())

    def pop(self) -> int:
        first = None
        while not self.stack1.empty():
            popped = self.stack1.pop()
            if not first:
                first = popped
            self.stack2.push(popped)

        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())
        if first:
            self.stack1.pop()
        return first

    def peek(self) -> int:
        first = None
        while not self.stack1.empty():
            popped = self.stack1.pop()
            if not first:
                first = popped
            self.stack2.push(popped)

        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())

        return first

    def empty(self) -> bool:
        return self.stack1.empty()


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return not bool(self.stack)

    def pop(self):
        return self.stack.pop(-1)


if __name__ == '__main__':
    obj = MyQueue()
    print(obj.empty())
    obj.push(1)
    obj.push(2)
    param = obj.peek()
    param = obj.pop()
    print(obj.empty())