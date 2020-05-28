from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildBST(left: int, right: int) -> TreeNode:
            if left < right:
                mid = (left + right) // 2
                root = TreeNode(nums[mid])
                root.left = buildBST(left, mid)
                root.right = buildBST(mid + 1, right)

                return root

        return buildBST(0, len(nums))


def main():
    s = Solution()
    print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
    print(s.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8]))

if __name__ == '__main__':
    main()
