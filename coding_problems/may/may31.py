from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def listCousins(self, root: TreeNode, val: int):
        if not root or root.val == val:
            return []

        queue = deque([root])
        found = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                children = [child for child in (node.left, node.right) if child]
                if all(child.val != val for child in children):
                    for child in children:
                        queue.append(child)
                else:
                    found = True

            if found:
                return [node.val for node in queue]

        return []


def main():
    s = Solution()

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, None, TreeNode(5)))
    print(s.listCousins(root, 5))
    print(s.listCousins(root, 4))
    print(s.listCousins(root, 6))
    print(s.listCousins(root, 1))

if __name__ == '__main__':
    main()
