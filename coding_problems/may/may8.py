import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        arr = [root]
        maxTuple = (-math.inf ,0)
        level = 1
        while arr:
            newArr = []
            levelSum = 0
            for node in arr:
                levelSum += node.val
                newArr += [child for child in (node.left, node.right) if child]
            
            maxTuple = max(maxTuple, (levelSum, level), key=lambda x: x[0])
            arr = newArr
            level += 1

        return maxTuple[1]


def main():
    s = Solution()

    root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))

    print(s.maxLevelSum(root))

if __name__ == '__main__':
    main()