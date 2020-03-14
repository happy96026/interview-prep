class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = ListNode(None)
        start.next = head
        iNode = start
        jNode = head

        while jNode:
            jNode = jNode.next
            if n > 0:
                n -= 1
            else:
                iNode = iNode.next

        iNode.next = iNode.next.next
        return start.next


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s = Solution()
    head = s.removeNthFromEnd(head, 3)
    print(head)

if __name__ == '__main__':
    main()