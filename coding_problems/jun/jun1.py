from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []

        d = { (i, i): [TreeNode(i)] for i in range(1, n + 1) }

        for j in range(2, n + 1):
            for i in reversed(range(1, j)):
                nodeList = []
                d[(i, j)] = nodeList
                for k in range(i, j + 1):
                    left = d[(i, k - 1)] if (i, k - 1) in d else [None]
                    right = d[(k + 1, j)] if (k + 1, j) in d else [None]
                    nodeList += [TreeNode(k, nodeL, nodeR) for nodeL in left for nodeR in right]

        return d[(1, n)]

def main():
    s = Solution()
    print(s.generateTrees(3))

if __name__ == '__main__':
    main()
