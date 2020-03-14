class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def printList(self):
    node = self
    output = ''
    while node != None:
      output += str(node.val)
      output += ' '
      node = node.next
    print(output)
  
  def reverseIteratively(self, head):
    node = head
    prevNode = None
    while node:
      nextNode = node.next
      node.next = prevNode
      prevNode = node
      node = nextNode

  def reverseRecursively(self, head):
    if head is None or head.next is None:
      return head
    
    reversedNode = self.reverseRecursively(head.next)
    head.next.next = head
    head.next = None
    return reversedNode

def main():
  testHead = ListNode(4)
  node1 = ListNode(3)
  testHead.next = node1
  node2 = ListNode(2)
  node1.next = node2
  node3 = ListNode(1)
  node2.next = node3
  testTail = ListNode(0)
  node3.next = testTail

  print('Initial list: ')
  testHead.printList()
  # testHead.reverseIteratively(testHead)
  testTail.reverseRecursively(testHead)
  print('List after reversal: ')
  testTail.printList()

if __name__ == '__main__':
  main()