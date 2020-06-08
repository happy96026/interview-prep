from typing import List
import math

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.val) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"

class Solution:
    def createTree(self, arr: List[int]) -> TreeNode:
        dummy = TreeNode(-math.inf)
        stack = [(dummy, True), (dummy, False)]
        hi = math.inf

        for n in reversed(arr):
            node = TreeNode(n)
            while True:
                parent, visited = stack.pop()
                if visited:
                    hi = parent.val

                if stack[-1][0].val < node.val < hi:
                    if visited:
                        parent.left = node
                    else:
                        parent.right = node
                    stack += [(node, True), (node, False)]
                    break
                
        return dummy.right


def main():
    s = Solution()
    print(s.createTree([1, 3, 2]))
    print(s.createTree([1, 4, 7, 6, 3, 13, 14, 10, 8]))


if __name__ == '__main__':
    main()
