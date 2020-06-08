class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isBalanced(root: TreeNode) -> int:
            if not root:
                return 0

            left = isBalanced(root.left)
            if left == -1:
                return -1

            right = isBalanced(root.right)
            if right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return isBalanced(root) > -1


def main():
    s = Solution()

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.isBalanced(root))

    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    print(s.isBalanced(root))

    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    print(s.isBalanced(root))

if __name__ == '__main__':
    main()
