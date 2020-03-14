# class Solution:
#   def calculate(self, s):
#     stack = []
#     sign = 1
#     _sum = operand = 0
#     for c in s:
#       if c.isdigit():
#         operand = 10 * operand + int(c)
#       elif c == '+':
#         _sum += sign * operand
#         operand = 0
#         sign = 1
#       elif c == '-':
#         _sum += sign * operand
#         operand = 0
#         sign = -1
#       elif c == '(':
#         stack.append((_sum, sign))
#         _sum = operand = 0
#         sign = 1
#       elif c == ')':
#         operand = sign * operand + _sum
#         _sum, sign = stack.pop()

#     return _sum + sign * operand

# class Solution:
#   def calculate(self, s):
#     stack = []
#     multiplier = 1
#     for c in reversed(s):
#       if c.isdigit():
#         stack.append(int(c) * multiplier)
#         multiplier *= 10
#       elif c == '(':
#         operand = self.evaluate_stack(stack)
#         stack.append(operand)
#       elif c != ' ':
#         stack.append(c)
#         multiplier = 1

#     return self.evaluate_stack(stack)
  
#   def evaluate_stack(self, stack):
#     _sum = 0
#     sign = 1
#     popped = None
#     while len(stack) > 0:
#       popped = stack.pop()
#       if popped == '+':
#         sign = 1
#       elif popped == '-':
#         sign = -1
#       elif popped == ')':
#         break
#       else:
#         _sum += sign * popped

#     return _sum

class Solution:
  def calculate(self, s):
    return self.recursive_eval(s)[1]

  def recursive_eval(self, s, i=0):
    _sum = operand = 0
    sign = 1
    while i < len(s):
      c = s[i]
      if c.isdigit():
        operand = 10 * operand + int(c)
      elif c == '(':
        i, operand = self.recursive_eval(s, i + 1)
      elif c == ')':
        break
      elif c != ' ':
        _sum += sign * operand
        sign = 1 if c == '+' else -1
        operand = 0
      i += 1

    return (i, _sum + sign * operand)

def main():
  s = Solution()
  print(s.calculate('100'))
  print(s.calculate('1 + -(((1)))'))
  print(s.calculate('-234560'))
  print(s.calculate('2-1 + 2'))
  print(s.calculate('-(-1)'))
  print(s.calculate('10 + 3+-(4+-  5)'))
  print(s.calculate('10+10'))
  print(s.calculate('(1+(4+5+2)-3)+(6+8)'))

if __name__ == '__main__':
  main()