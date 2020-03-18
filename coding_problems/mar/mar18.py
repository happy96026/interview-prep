from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        DFS Recursive
        Time Complexity: O(n)
        Space Complexity: O(log n)
        '''
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

    # def maxDepth(self, root: TreeNode) -> int:
    #     '''
    #     DFS Iterative
    #     Time Complexity: O(n)
    #     Space Complexity: O(log n)
    #     '''
    #     if not root:
    #         return 0

    #     stack = [(root, 1)]
    #     maxDepth = 0
    #     while stack:
    #         node, depth = stack.pop()

    #         if node:
    #             maxDepth = max(maxDepth, depth)
    #             stack.append((node.left, depth + 1))
    #             stack.append((node.right, depth + 1))

    #     return maxDepth

    # def maxDepth(self, root: TreeNode) -> int:
    #     '''
    #     BFS
    #     Time Complexity: O(n)
    #     Space Complexity: O(n)
    #     '''
    #     if not root:
    #         return 0
        
    #     queue = deque([(root, 1)])
    #     maxDepth = 0
    #     while queue:
    #         node, depth = queue.popleft()

    #         if node:
    #             maxDepth = depth
    #             queue.append((node.left, depth + 1))
    #             queue.append((node.right, depth + 1))
        
    #     return maxDepth


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.maxDepth(root))

if __name__ == '__main__':
    main()