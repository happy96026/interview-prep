from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def getSubtreeSum(root, table):
            if not root:
                return 0

            leftSum = getSubtreeSum(root.left, table)
            rightSum = getSubtreeSum(root.right, table)

            totalSum = leftSum + rightSum + root.val
            if totalSum not in table:
                table[totalSum] = 0
            table[totalSum] += 1

            return totalSum

        table = {}
        getSubtreeSum(root, table)

        result = []
        maxFreq = 0
        for k, v in table.items():
            if v > maxFreq:
                result = [k]
                maxFreq = v
            elif v == maxFreq:
                result.append(k)

        return result


def main():
    s = Solution()

    root = TreeNode(5, left=TreeNode(2), right=TreeNode(-3))
    print(s.findFrequentTreeSum(root))

    root = TreeNode(5, left=TreeNode(2), right=TreeNode(-5))
    print(s.findFrequentTreeSum(root))

    root = TreeNode(3, left=TreeNode(1), right=TreeNode(-3))
    print(s.findFrequentTreeSum(root))

if __name__ == '__main__':
    main()
