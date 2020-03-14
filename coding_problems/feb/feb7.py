class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def add_two_numbers(self, l1, l2, c = 0):
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    digit = val1 + val2
    next_c = 0
    if digit >= 10:
      digit -= 10
      next_c = 1
    solution_node = ListNode(digit + c)
    next1 = l1.next if l1 else None
    next2 = l2.next if l2 else None

    if (next1 or next2):
      solution_node.next = self.add_two_numbers(next1, next2, next_c)

    return solution_node

def main():
  l1 = ListNode(2)
  l1.next = ListNode(4)
  l1.next.next = ListNode(3)

  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(4)

  result = Solution().add_two_numbers(l1, l2)
  while result:
    print(result.val)
    result = result.next

if __name__ == '__main__':
  main()