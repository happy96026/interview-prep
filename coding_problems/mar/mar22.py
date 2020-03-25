from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def valuesAtHeight(self, root: TreeNode, height: int) -> List[int]:
    #     if not root or height < 1:
    #         return []

    #     queue = deque([root])
    #     for _ in range(height - 1):
    #         if not queue:
    #             break
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)

    #     return [node.val for node in queue]

    def valuesAtHeight(self, root: TreeNode, height: int) -> List[int]:
        stack = [(root, 1)]
        values = []
        while stack:
            node, nodeHeight = stack.pop()
            if node:
                if nodeHeight == height:
                    values.append(node.val)
                stack.append((node.right, nodeHeight + 1))
                stack.append((node.left, nodeHeight + 1))

        return values

                
def main():
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print(s.valuesAtHeight(root, 1))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    print(s.valuesAtHeight(root, 3))

if __name__ == '__main__':
    main()