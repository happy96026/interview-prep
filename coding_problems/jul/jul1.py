import math

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevel(self, root):
        if not root:
            return 0

        maxLevel = 0
        maxSum = -math.inf

        arr = [root]
        level = 0
        while arr:
            newArr = []
            _sum = 0
            for node in arr:
                _sum += node.val
                for child in (node.left, node.right):
                    if child:
                        newArr.append(child)

            if _sum > maxSum:
                maxLevel = level
                maxSum = _sum

            level += 1
            arr = newArr

        return maxLevel


def main():
    s = Solution()

    root = TreeNode(1, TreeNode(5, TreeNode(4), TreeNode(-1)), TreeNode(4, TreeNode(3), TreeNode(2)))
    print(s.maxLevel(root))

if __name__ == '__main__':
    main()
