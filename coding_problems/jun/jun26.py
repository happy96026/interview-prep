class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"

class Solution:
    def inorderSucessor(self, node: TreeNode) -> TreeNode:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        else:
            parent = node.parent
            while parent and parent.value < node.value:
                node = parent
                parent = node.parent

            return parent


def main():
    s = Solution()

    tree = TreeNode(3)
    tree.left = TreeNode(2)
    tree.right = TreeNode(4)
    tree.left.parent = tree
    tree.right.parent = tree
    tree.left.left = TreeNode(1)
    tree.left.left.parent = tree.left
    tree.right.right = TreeNode(5)
    tree.right.right.parent = tree.right
    print(s.inorderSucessor(tree.left))
    print(s.inorderSucessor(tree.right))

    tree = TreeNode(3)
    tree.left = TreeNode(2)
    tree.right = TreeNode(6)
    tree.left.parent = tree
    tree.right.parent = tree
    tree.right.left = TreeNode(4)
    tree.right.left.parent = tree.right
    tree.right.left.right = TreeNode(5)
    tree.right.left.right.parent = tree.right.left
    print(s.inorderSucessor(tree.left))
    print(s.inorderSucessor(tree.right.left.right))

if __name__ == '__main__':
    main()
