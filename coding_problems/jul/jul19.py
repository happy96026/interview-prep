import unittest
from typing import List

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"

        return f"({self.value})"


class Solution(unittest.TestCase):
    def splitBST(self, bst: TreeNode, s: int) -> List[TreeNode]:
        leftSubtree = TreeNode(None)
        rightSubtree = TreeNode(None)

        node = bst
        left = leftSubtree
        right = rightSubtree
        while node:
            if node.value <= s:
                left.right = node
                left = node
                node = node.right
                left.right = None
            else:
                right.left = node
                right = node
                node = node.left
                right.left = None

        return [leftSubtree.right, rightSubtree.left]

    def test_1(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4, None, TreeNode(5)))
        left, right = self.splitBST(root, 1)
        self.assertTrue(all([str(left) == '(1)', str(right) == '(3, (2), (4, None, (5)))']))

    def test_2(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4, None, TreeNode(5)))
        left, right = self.splitBST(root, 2)
        self.assertTrue(all([str(left) == '(1, None, (2))', str(right) == '(3, None, (4, None, (5)))']))

    def test_3(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4, None, TreeNode(5)))
        left, right = self.splitBST(root, 3)
        self.assertTrue(all([str(left) == '(3, (1, None, (2)))', str(right) == '(4, None, (5))']))

    def test_4(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4, None, TreeNode(5)))
        left, right = self.splitBST(root, 4)
        self.assertTrue(all([str(left) == '(3, (1, None, (2)), (4))', str(right) == '(5)']))

    def test_5(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4, None, TreeNode(5)))
        left, right = self.splitBST(root, 5)
        self.assertTrue(all([str(left) == '(3, (1, None, (2)), (4, None, (5)))', str(right) == 'None']))

    def test_6(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
        left, right = self.splitBST(root, 2)
        self.assertTrue(all([str(left) == '(2, (1))', str(right) == '(4, (3), (6, (5), (7)))']))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
