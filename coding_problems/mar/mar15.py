from collections import deque
from typing import List

class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        nodes = deque([self])
        arr = []
        while len(nodes):
            node = nodes.popleft()
            if not node:
                arr.append(None)
            else:
                arr.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)

        last = 0
        for i, x in enumerate(arr, start=1):
            if x:
                last = i
        
        return str(arr[:last])

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.getBstIterative(nums)

    def getBstRecursive(self, nums: List[int], start: int, end: int) -> TreeNode:
        '''
        Time Complexity: O(n)
        Space Complexity: O(log n)
        start is inclusive, end is exclusive
        '''
        if end - start < 1:
            node = None
        elif end - start < 2:
            node = TreeNode(nums[start])
        else:
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = self.getBst(nums, start, mid)
            node.right = self.getBst(nums, mid + 1, end)

        return node

    # def getBstIterative(self, nums: List[int]) -> TreeNode:
    #     '''
    #     Time Complexity: O(n)
    #     Space Complexity: O(n)
    
    #     start and end are both inclusive
    #     '''
    #     queue = deque([(0, len(nums) - 1)])
    #     nodes = []
    #     while queue:
    #         start, end = queue.popleft()

    #         if start > end:
    #             nodes.append(None)
    #         else:
    #             mid = (start + end) // 2
    #             nodes.append(TreeNode(nums[mid]))
    #             queue.append((start, mid - 1))
    #             queue.append((mid + 1, end))

    #     for i, node in enumerate(nodes):
    #         left, right = 2*i + 1, 2*i + 2

    #         if node:
    #             if left < len(nodes):
    #                 node.left = nodes[left]
    #             if right < len(nodes):
    #                 node.right = nodes[right]

    #     return nodes[0]

    def getBstIterative(self, nums: List[int]) -> TreeNode:
        '''
        Time Complexity: O(n)
        Space Complexity: O(log n)

        start and end are both inclusive
        '''
        if not nums:
            return None

        root = TreeNode(0)
        stack = [(root, 0, len(nums))]

        while stack:
            node, start, end = stack.pop()
            mid = (start + end) // 2
            node.val = nums[mid]

            if mid + 1 < end:
                node.right = TreeNode(0)
                stack.append((node.right, mid + 1, end))
            
            if start < mid:
                node.left = TreeNode(0)
                stack.append((node.left, start, mid))

        return root


def main():
    s = Solution()
    # print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
    # print(s.sortedArrayToBST([]))
    print(s.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7, 8]))

if __name__ == '__main__':
    main()
