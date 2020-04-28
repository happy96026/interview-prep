from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            num = len(q)
            while num > 0:
                n = q.popleft()
                result += str(n.value)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                num = num - 1
            if len(q):
                result += "\n"

        return result

class Solution:
    def fullBinaryTree(self, node):
        if not node:
            return
        
        left = self.singleChild(node.left)
        right = self.singleChild(node.right)

        if left:
            node.left = left
        if right:
            node.right = right
        
        self.fullBinaryTree(node.left)
        self.fullBinaryTree(node.right)

        return node

    def singleChild(self, node):
        if node:
            if node.left and not node.right:
                return node.left
            elif not node.left and node.right:
                return node.right

        return None


def main():
    s = Solution()
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.right.right = Node(4)
    tree.right.left = Node(9)
    tree.left.left = Node(0)
    print(s.fullBinaryTree(tree))

if __name__ == '__main__':
    main()