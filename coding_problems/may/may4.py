class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = ListNode(None, head)
        prev = None
        curr = fast = dummy
        length = -1

        while fast:
            if fast.next:
                fast = fast.next.next
                length += 2
            else:
                length += 1
                fast = fast.next

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left = prev
        right = curr.next if length % 2 == 1 else curr

        while left is not dummy:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True


def main():
    s = Solution()

    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(s.isPalindrome(head))

    head = ListNode(1, ListNode(2, ListNode(2, ListNode(3))))
    print(s.isPalindrome(head))

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print(s.isPalindrome(head))

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(2)))))
    print(s.isPalindrome(head))

if __name__ == '__main__':
    main()