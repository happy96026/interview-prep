import math

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxPath = -math.inf

        def maxPathSum(root):
            nonlocal maxPath

            if not root:
                return 0

            left = maxPathSum(root.left)
            right = maxPathSum(root.right)
            maxPath = max(maxPath, left + root.val + right)
            return max(0, root.val + left, root.val + right)

        maxPathSum(root)
        return maxPath


def main():
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(-25)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(4)
    print(s.maxPathSum(root))

if __name__ == '__main__':
    main()