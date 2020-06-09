class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        slow = head
        length = 1
        while slow.next:
            slow = slow.next
            length += 1
        slow.next = head

        fast = head
        for _ in range(k % length):
            fast = fast.next

        while fast is not head:
            slow = slow.next
            fast = fast.next

        head = slow.next
        slow.next = None

        return head


def main():
    s = Solution()

    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.rotateRight(root, 2).val)

    root = ListNode(0, ListNode(1, ListNode(2)))
    print(s.rotateRight(root, 4).val)

if __name__ == '__main__':
    main()
