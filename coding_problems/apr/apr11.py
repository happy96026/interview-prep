class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        result = ''
        result += str(self.val) + ' ' + str(self.left) + ' ' + str(self.right)
        return result
        
class Codec:
    # def serialize(self, root: TreeNode) -> str:
    #     def preorder(root):
    #         if not root:
    #             return ['#']
    #         return [str(root.val)] + preorder(root.left) + preorder(root.right)

    #     return ' '.join(preorder(root))

    # def deserialize(self, data: str) -> TreeNode:
    #     arr = data.split(' ')

    #     def generator():
    #         for n in arr:
    #             yield n if n == '#' else int(n)
    #     g = generator()

    #     def deserialize():
    #         n = next(g)
    #         if n == '#':
    #             return None
            
    #         node = TreeNode(n)
    #         node.left = deserialize()
    #         node.right = deserialize()
    #         return node

    #     return deserialize()

    def serialize(self, root: TreeNode) -> str:
        stack = [root]
        arr = []

        while stack:
            node = stack.pop()
            if node:
                arr.append(str(node.val))
                stack += [node.right, node.left]
            else:
                arr.append('#')

        return ' '.join(arr)

    def deserialize(self, data: str) -> TreeNode:
        arr = data.split(' ')
        dummy = TreeNode(None)
        stack = [(dummy, True)]

        for n in arr:
            currNode, isLeft = stack.pop()
            if n == '#':
                newNode = None
            else:
                newNode = TreeNode(int(n))
                stack += [(newNode, False), (newNode, True)]
            
            if isLeft:
                currNode.left = newNode
            else:
                currNode.right = newNode

        return dummy.left
                

def main():
    c = Codec()

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(4)
    root.right.right = TreeNode(7)

    data = c.serialize(root)
    node = c.deserialize(data)

    print(data)
    print(node)


if __name__ == '__main__':
    main()