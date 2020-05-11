class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dummy = ListNode(None)
        dummy.next = head

        slow = fast = dummy

        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next

            if fast and slow is fast:
                return True

        return False


def main():
    s = Solution()

    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(s.hasCycle(head))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    print(s.hasCycle(head))

    head = ListNode(1)
    print(s.hasCycle(head))

    head = ListNode(4)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(0)
    head.next.next.next.next.next = head.next
    print(s.hasCycle(head))

    print(s.hasCycle(None))

if __name__ == '__main__':
    main()