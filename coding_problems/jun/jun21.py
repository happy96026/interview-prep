class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        _str = ''
        node = self
        while node:
            _str += str(node.val) + '->'
            node = node.next

        return _str[:-2]

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        node = dummy

        while True:
            if not node.next or not node.next.next:
                break

            first = node.next
            second = node.next.next
            first.next = second.next
            second.next = first
            node.next = second
            node = first

        return dummy.next



def main():
    s = Solution()
    print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))

if __name__ == '__main__':
    main()
