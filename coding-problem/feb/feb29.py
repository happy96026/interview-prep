class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def prettyPrint(self):
    c = self
    while c:
      print(c.val, end=' ')
      c = c.next
    print()

# class Solution:
#   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#     lenA = self.getLen(headA)
#     lenB = self.getLen(headB)

#     nodeA = headA
#     nodeB = headB
#     if lenA > lenB:
#       for _ in range(lenA - lenB):
#         nodeA = nodeA.next
#     elif lenB > lenA:
#       for _ in range(lenB - lenA):
#         nodeB = nodeB.next
    
#     while nodeA:
#       if nodeA is nodeB:
#         return nodeA
#       else:
#         nodeA = nodeA.next
#         nodeB = nodeB.next

#     return nodeA

#   def getLen(self, node):
#     length = 0
#     while node:
#       node = node.next
#       length += 1

#     return length

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if not (headA and headB):
      return None

    nodeA = headA
    nodeB = headB

    looped = [False, False]
    while not all(looped):
      nodeA = nodeA.next
      nodeB = nodeB.next

      if nodeA is None:
        nodeA = headB
        looped[0] = True
      elif nodeB is None:
        nodeB = headA
        looped[1] = True

    while nodeA:
      if nodeA is nodeB:
        return nodeA
      nodeA = nodeA.next
      nodeB = nodeB.next
      
    return nodeA


def main():
  a = ListNode(1)
  a.next = ListNode(2)
  a.next.next = ListNode(3)
  a.next.next.next = ListNode(4)

  b = ListNode(6)
  b.next = a.next.next

  s = Solution()
  c = s.getIntersectionNode(a, b)
  c.prettyPrint()

if __name__ == '__main__':
  main()