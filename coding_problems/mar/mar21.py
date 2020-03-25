import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def isValidBst(root, minVal = -math.inf, maxVal = math.inf):
    #         if not root:
    #             return True
    #         elif not (minVal < root.val < maxVal):
    #             return False
    #         else:
    #             return isValidBst(root.left, minVal, root.val) and isValidBst(root.right, root.val, maxVal)
            
    #     return isValidBst(root)

    # def isValidBST(self, root: TreeNode) -> bool:
    #     def getInOrder(root, order = []):
    #         if root:
    #             getInOrder(root.left)
    #             order.append(root.val)
    #             getInOrder(root.right)

    #         return order

    #     inOrder = getInOrder(root)
    #     for i in range(len(inOrder) - 1):
    #         if inOrder[i] >= inOrder[i + 1]:
    #             return False

    #     return True

    # def isValidBST(self, root: TreeNode) -> bool:
    #     stack = []
    #     minVal = -math.inf

    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left

    #         if stack:
    #             root = stack.pop()
    #             if minVal >= root.val:
    #                 return False
    #              minVal = root.val
    #             root = root.right

    #     return True

    def isValidBST(self, root: TreeNode) -> bool:
        minVal = -math.inf
        def getInOrder(root):
            nonlocal minVal

            if root:
                if not getInOrder(root.left):
                    return False
                if minVal >= root.val:
                    return False
                minVal = root.val
                if not getInOrder(root.right):
                    return False

            return True

        return getInOrder(root)



def main():
    s = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(s.isValidBST(root))

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(s.isValidBST(root))

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.left.right = TreeNode(5)
    print(s.isValidBST(root))

if __name__ == '__main__':
    main()