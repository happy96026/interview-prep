class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def preorder(self):
    print(self.value, end=' ')
    if self.left:
      self.left.preorder()
    if self.right:
      self.right.preorder()

class Solution:
  def invert(self, node):
    tempNode = node.left
    node.left = node.right
    node.right = tempNode
    if node.left:
      self.invert(node.left)
    if node.right:
      self.invert(node.right)

def main():
  root = Node('a')
  root.left = Node('b')
  root.right = Node('c')
  root.left.left = Node('d')
  root.left.right = Node('e')
  root.right.left = Node('f')

  root.preorder()
  print()
  Solution().invert(root)
  root.preorder()
  print()

if __name__ == '__main__':
  main()