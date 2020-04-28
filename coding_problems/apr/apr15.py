class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        if not self.minStack or self.getMin() >= x:
            self.minStack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.minStack.pop()

        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


def main():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())

if __name__ == '__main__':
    main()
