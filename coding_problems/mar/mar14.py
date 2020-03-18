from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        c = self
        answer = []
        while c:
            answer.append(c.val)
            c = c.next
        return str(answer)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        print(lists[0])


def main():
    s = Solution()

    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)

    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)

    c = ListNode(2)
    c.next = ListNode(6)

    print(s.mergeKLists([a, b, c]))


if __name__ == '__main__':
    main()