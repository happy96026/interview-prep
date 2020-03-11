class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  node = None

  if root_node is None:
    return (floor, ceil)
  elif root_node.value > k:
    node = root_node.left
    if ceil is None or root_node.value < ceil:
      ceil = root_node.value
  else:
    node = root_node.right
    if floor is None or root_node.value > floor:
      floor = root_node.value

  return findCeilingFloor(node, k, floor, ceil)


def main():
  root = Node(8)
  root.left = Node(4)
  root.right = Node(12)

  root.left.left = Node(2)
  root.left.right = Node(6)

  root.right.left = Node(10)
  root.right.right = Node(14)

  print(findCeilingFloor(root, 5))

if __name__ == '__main__':
  main()