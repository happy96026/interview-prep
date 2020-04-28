class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = None

class Solution:
    def isSymmetric(self, root):
        children = root.children
        if not children:
            return True

        i = 0
        j = len(children) - 1
        while i < j:
            if not self.nodesSymmetric(children[i], children[j]):
                return False
            i += 1
            j -= 1

        if i == j:
            if not self.isSymmetric(children[i]):
                return False

        return True
    
    def nodesSymmetric(self, node1, node2):
        children1 = node1.children if node1.children else []
        children2 = node2.children if node2.children else []

        if node1.val != node2.val or len(children1) != len(children2):
            return False
        
        for i in range(len(children1)):
            if not self.nodesSymmetric(children1[i], children2[-1 - i]):
                return False

        return True
    

def main():
    s = Solution()

    root = TreeNode(4)
    root.children = [TreeNode(3), TreeNode(3)]
    root.children[0].children = [TreeNode(9), TreeNode(4), TreeNode(1)]
    root.children[1].children = [TreeNode(1), TreeNode(4), TreeNode(9)]

    print(s.isSymmetric(root))

if __name__ == '__main__':
    main()