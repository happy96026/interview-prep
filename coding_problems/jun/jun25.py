from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode) -> List[int]:
        maxPath = None
        maxVal = -math.inf

        path = []
        def dfs(node: TreeNode, val: int) -> bool:
            nonlocal maxVal, maxPath

            if not node:
                return False

            path.append(node)
            val += node.val
            if not dfs(node.left, val) and not dfs(node.right, val) and val > maxVal:
                maxVal = val
                maxPath = [x for x in path]

            path.pop()
            return True

        dfs(root, 0)

        return [node.val for node in maxPath]


def main():
    s = Solution()
    print(s.hasPathSum(TreeNode(1, TreeNode(3, None, TreeNode(5)), TreeNode(2, TreeNode(4)))))

if __name__ == '__main__':
    main()
