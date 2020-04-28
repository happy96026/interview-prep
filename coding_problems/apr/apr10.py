class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def evaluate(self, root: Node) -> float:
        if not root:
            return 0
        
        if root.val not in ['+', '-', '*', '/']:
            return root.val

        left, right = self.evaluate(root.left), self.evaluate(root.right)
        
        if root.val == '+':
            return left + right
        elif root.val == '-':
            return left - right
        elif root.val == '*':
            return left * right
        else:
            return left / right


def main():
    s = Solution()

    root = Node('*')
    root.left = Node('+')
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right = Node('+')
    root.right.left = Node(4)
    root.right.right = Node(5)

    print(s.evaluate(root))

if __name__ == '__main__':
    main()