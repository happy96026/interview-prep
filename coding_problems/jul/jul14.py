import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getArray(self):
        arr = []
        node = self
        while node:
            arr.append(node.val)
            node = node.next

        return arr

class Solution(unittest.TestCase):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

    def test_1(self):
        node = self.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))
        arr = node.getArray() if node else []
        self.assertSequenceEqual(arr, [1, 2])

    def test_2(self):
        node = self.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))
        arr = node.getArray() if node else []
        self.assertSequenceEqual(arr, [1, 2, 3])

    def test_3(self):
        node = self.deleteDuplicates(ListNode(1, ListNode(2, ListNode(3))))
        arr = node.getArray() if node else []
        self.assertSequenceEqual(arr, [1, 2, 3])

    def test_4(self):
        node = self.deleteDuplicates(None)
        arr = node.getArray() if node else []
        self.assertSequenceEqual(arr, [])



def main():
    unittest.main()

if __name__ == '__main__':
    main()
