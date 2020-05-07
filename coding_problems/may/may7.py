class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     if root:
    #         left = self.lowestCommonAncestor(root.left, p, q)
    #         right = self.lowestCommonAncestor(root.right, p, q)

    #         if left and right or root in [p, q]:
    #             return root
    #         else:
    #             return left or right

    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     d = { root: None }
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         for child in (node.left, node.right):
    #             if child:
    #                 d[child] = node
    #                 stack.append(child)

    #     s = set()
    #     node = p
    #     while node in d:
    #         s.add(node)
    #         node = d[node]

    #     node = q
    #     while node in d:
    #         if node in s:
    #             return node
    #         node = d[node]

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [(root, 0)]
        i = 0
        found = 0

        while found < 2:
            node, state = stack.pop()
            if node:
                if state == 0 and node in [p, q]:
                    found += 1
                    if found == 1:
                        i = len(stack)

                if state == 0:
                    stack += [(node, 1), (node.left, 0)]
                elif state == 1:
                    stack += [(node, 2), (node.right, 0)]
                else:
                    i = min(i, len(stack) - 1)
                
        return stack[i][0]


def main():
    s = Solution()

    root = TreeNode(3)

    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print(s.lowestCommonAncestor(root, root.left, root.right).val)
    print(s.lowestCommonAncestor(root, root.left, root.left.right.right).val)


if __name__ == '__main__':
    main()