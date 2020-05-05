from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        levelOrder = []
        arr = [root]
        while arr:
            levelOrder.append([node.val for node in arr])
            arr = [node for parent in arr for node in (parent.left, parent.right) if node]

        return levelOrder


def main():
    s = Solution()

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.levelOrder(root))

if __name__ == '__main__':
    main()