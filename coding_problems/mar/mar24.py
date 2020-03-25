class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # def countUnivalSubtrees(self, root: TreeNode) -> int:
    #     '''
    #     DFS
    #     Time Complexity: O(n)
    #     Space Complexity: O(n)
    #     '''
    #     count = 0
    #     def countUnivalSubtrees(root: TreeNode) -> bool:
    #         nonlocal count
    #         result = all([countUnivalSubtrees(child) and child.val == root.val  for child in (root.left, root.right) if child])
    #         if result: count += 1
    #         return result

    #     if not root:
    #         return 0

    #     countUnivalSubtrees(root)
    #     return count

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        '''
        DFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        count = 0
        def countUnivalSubtrees(root: TreeNode, val: int = None) -> bool:
            nonlocal count

            if not root: return True
            if not all([countUnivalSubtrees(child, root.val) for child in (root.left, root.right)]): return False
                
            count += 1
            return root.val == val

        countUnivalSubtrees(root)
        return count


def main():
    s = Solution()

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(0)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    print(s.countUnivalSubtrees(root))

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    print(s.countUnivalSubtrees(root))

    root = TreeNode(5)
    print(s.countUnivalSubtrees(root))

    print(s.countUnivalSubtrees(None))

if __name__ == '__main__':
    main()
    