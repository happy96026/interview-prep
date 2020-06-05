from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        levels = [[root]]
        left = False
        while True:
            arr = []
            for node in reversed(levels[-1]):
                children = [node.left, node.right]
                if not left:
                    children = reversed(children)
                for child in children:
                    if child:
                        arr.append(child)

            if not arr:
                break

            levels.append(arr)
            left = not left

        return [[node.val for node in level] for level in levels]


def main():
    s = Solution()

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.zigzagLevelOrder(root))

if __name__ == '__main__':
    main()
