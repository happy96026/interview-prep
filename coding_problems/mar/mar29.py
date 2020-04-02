import math

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        answer = str(self.val)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)

        return answer

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> TreeNode:
        maxCount = 0
        result = None

        def largestBSTSubtree(root):
            nonlocal maxCount, result

            if root:
                left = largestBSTSubtree(root.left)
                right = largestBSTSubtree(root.right)
                if left and left[2] < root.val and right and root.val < right[1]:
                    currCount = left[0] + right[0] + 1
                    if currCount > maxCount:
                        maxCount = currCount
                        result = root

                    return (currCount, min(root.val, left[1]), max(root.val, right[2]))
                else:
                    return None
            else:
                return (0, math.inf, -math.inf)

        largestBSTSubtree(root)
        return result


def main():
    s = Solution()

    node = TreeNode(5)
    node.left = TreeNode(6)
    node.right = TreeNode(7)
    node.left.left = TreeNode(2)
    node.right.left = TreeNode(4)
    node.right.right = TreeNode(9)
    print(s.largestBSTSubtree(node))

    node = TreeNode(5)
    node.left = TreeNode(1)
    node.right = TreeNode(4)
    node.right.left = TreeNode(3)
    node.right.right = TreeNode(6)
    print(s.largestBSTSubtree(node))

    node = TreeNode(5)
    node.left = TreeNode(3)
    node.right = TreeNode(7)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(4)
    node.right.left = TreeNode(6)
    print(s.largestBSTSubtree(node))

if __name__ == '__main__':
    main()