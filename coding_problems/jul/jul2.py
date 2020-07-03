from typing import Set

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False

        sSerial = self.serialize(s)
        tSerial = self.serialize(t)
        
        return tSerial in sSerial

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ',#'

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f',{root.val}{left}{right}'


def main():
    s = Solution()
    print(s.isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2))))
    print(s.isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2))))
    print(s.isSubtree(TreeNode(1, TreeNode(4, TreeNode(3), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(-1))), TreeNode(4, TreeNode(3), TreeNode(2))))

if __name__ == '__main__':
    main()
