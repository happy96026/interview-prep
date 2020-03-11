class MaxStack:
  def __init__(self):
    self.history = []
    self.stack = []

  def push(self, val):
    if len(self.history) == 0:
      self.history.append(val)
    elif val >= self.history[-1]:
      self.history.append(val)
    self.stack.append(val)

  def pop(self):
    popped = None
    if len(self.stack) > 0:
      popped = self.stack.pop()
      if popped == self.history[-1]:
        self.history.pop()

    return popped

  def max(self):
    return self.history[-1] if len(self.history) > 0 else None


def main():
  s = MaxStack()
  s.push(1)
  s.push(2)
  s.push(3)
  s.push(2)
  print(s.max())
  s.pop()
  s.pop()
  print(s.max())

if __name__ == '__main__':
  main()