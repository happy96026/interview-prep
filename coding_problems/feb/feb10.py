class Solution:
  def isValid(self, s):
    d = {
      ')': '(',
      '}': '{',
      ']': '['
    }
    stack = []

    for c in s:
      if c not in d:
        stack.append(c)
      else:
        popped = stack.pop()
        if d[c] != popped:
          return False

    return len(stack) == 0

def main():
  solution = Solution()
  s = '()(){(())'
  print(solution.isValid(s))
  s = ''
  print(solution.isValid(s))
  s = '([{}])()'
  print(solution.isValid(s))

if __name__ == '__main__':
  main()