from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        queue = deque([self])
        s = ''
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    s += node.val
                    queue.append(node.left)
                    queue.append(node.right)
            s += '\n'

        return s


def main():
    tree = Node('a')
    tree.left = Node('b')
    tree.right = Node('c')
    tree.left.left = Node('d')
    tree.left.right = Node('e')
    tree.right.left = Node('f')
    tree.right.right = Node('g')
    print(tree)

if __name__ == '__main__':
    main()
