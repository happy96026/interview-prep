class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        arr = [self]
        _str = ''

        while arr:
            new = []
            for node in arr:
                if node:
                    _str += str(node.val) + ', '
                    if node.left or node.right:
                        new += [node.left, node.right]
                else:
                    _str += str(node) + ', '
            arr = new

        return _str[:-2]

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        return None if self.postOrderTraversal(root, target) else root

    def postOrderTraversal(self, root: TreeNode, target: int) -> bool:
        if not root:
            return True

        if self.postOrderTraversal(root.left, target):
            root.left = None
        if self.postOrderTraversal(root.right, target):
            root.right = None

        return (root.val == target and not root.left and not root.right)


def main():
    s = Solution()

    print(s.removeLeafNodes(TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3, TreeNode(2), TreeNode(4))), 2))
    print(s.removeLeafNodes(TreeNode(1, TreeNode(3, TreeNode(3), TreeNode(2)), TreeNode(3)), 3))
    print(s.removeLeafNodes(TreeNode(1, TreeNode(2, TreeNode(2, TreeNode(2)))), 2))
    print(s.removeLeafNodes(TreeNode(1, TreeNode(1), TreeNode(1)), 1))
    print(s.removeLeafNodes(TreeNode(1, TreeNode(2), TreeNode(3)), 1))

if __name__ == '__main__':
    main()
