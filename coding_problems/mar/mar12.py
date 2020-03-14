class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        try:
            return self.stack2.pop()
        except IndexError as err:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

if __name__ == '__main__':
    main()