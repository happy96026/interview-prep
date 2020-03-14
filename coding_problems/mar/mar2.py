class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: Node) -> Node:
        d = {}
        node = head
        _sum = 0
        while node:
            _sum += node.val
            d[_sum] = node
            node = node.next

        node = head
        _sum = 0
        while node:
            _sum += node.val
            if _sum == 0:
                head = node.next
            elif d[_sum] is not node:
                node.next = d[_sum].next
            node = node.next
        
        return head


def main():
    node = Node(1)
    node.next = Node(-1)
    # node.next.next = Node(-3)
    # node.next.next.next = Node(-3)
    # node.next.next.next.next = Node(1)
    # node.next.next.next.next.next = Node(4)
    # node.next.next.next.next.next.next = Node(-4)
    s = Solution()
    node = s.removeZeroSumSublists(node)
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

if __name__ == '__main__':
    main()