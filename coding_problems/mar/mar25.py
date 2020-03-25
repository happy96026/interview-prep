from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     '''
    #     DFS Iterative
    #     Time Complexity: O(n)
    #     Space Complexity: O(n)
    #     '''
    #     if len(preorder) < 1:
    #         return None

    #     d = { v: i for i, v in enumerate(inorder) }

    #     root = TreeNode(preorder[0])
    #     stack = [
    #         (root, False, d[root.val], len(inorder)),
    #         (root, True, -1, d[root.val])
    #     ]
    #     for i in range(1, len(preorder)):
    #         while True:
    #             node, isLeft, minVal, maxVal = stack.pop()
    #             if minVal + 1 < maxVal:
    #                 child = TreeNode(preorder[i])
    #                 if isLeft:
    #                     node.left = child
    #                 else:
    #                     node.right = child
    #                 stack.append((child, False, d[child.val], maxVal))
    #                 stack.append((child, True, minVal, d[child.val]))
    #                 break

    #     return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        DFS Recursive
        Time Complexity: O(n)
        Space Compleixty: O(n)
        '''
        d = { v: i for i, v in enumerate(inorder) }
        preorderIter = iter(preorder)
        def buildTree(minVal: int = -1, maxVal: int = len(inorder)) -> TreeNode:
            if minVal + 1 == maxVal:
                return None

            node = TreeNode(next(preorderIter))
            node.left = buildTree(minVal, d[node.val])
            node.right = buildTree(d[node.val], maxVal)

            return node

        return buildTree()


def main():
    s = Solution()
    root = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(root.val)
    print(root.left.val)
    print(root.left.left)
    print(root.left.right)
    print(root.right.val)
    print(root.right.left.val)
    print(root.right.right.val)

if __name__ == '__main__':
    main()