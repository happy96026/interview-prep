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
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     '''
    #     Compare one by one
    #     m is length of lists and n is the number of all nodes
    #     Time Complexity: O(mn)
    #     Space Complexity: O(1)
    #     '''
    #     head = ListNode(None)
    #     node = head
    #     while any(lists):
    #         minIndex = min((i for i in range(len(lists)) if lists[i]), key=lambda i: lists[i].val)
    #         node.next = lists[minIndex]
    #         node = node.next
    #         lists[minIndex] = node.next

    #     return head.next

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     '''
    #     Brute Force
    #     n is the number of all nodes
    #     Time Complexity: O(nlogn)
    #     Space Complexity: O(n)
    #     '''
    #     arr = []
    #     for head in lists:
    #         while head:
    #             arr.append(head)
    #             head = head.next

    #     if not arr: return None
    #     arr.sort(key=lambda node: node.val)
    #     head = arr[0]
    #     node = head
    #     for i in range(1, len(arr)):
    #         node.next = arr[i]
    #         node = node.next

    #     return head

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     '''
    #     Merge Two Sorted List
    #     m is the length of lists and n is the number of all nodes
    #     Time Complexity: O(mn)
    #     Space Complexity: O(1)
    #     '''
    #     head = ListNode(None)
    #     for i in range(len(lists)):
    #         currNode = head
    #         node1, node2 = currNode.next, lists[i]

    #         while node1 and node2:
    #             if node1.val <= node2.val:
    #                 currNode.next = node1
    #                 node1 = node1.next
    #             else:
    #                 currNode.next = node2
    #                 node2 = node2.next
    #             currNode = currNode.next
            
    #         while node1:
    #             currNode.next = node1
    #             node1 = node1.next
    #             currNode = currNode.next

    #         while node2:
    #             currNode.next = node2
    #             node2 = node2.next
    #             currNode = currNode.next

    #     return head.next
        
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     '''
    #     Heap
    #     m is the length of lists and n is the number of all nodes
    #     Time Complexity: O(nlog(m))
    #     Space Complexity: O(m)
    #     '''
    #     def heapify(arr, key=lambda x: x):
    #         for i in reversed(range(len(arr))):
    #             siftDown(arr, i, len(arr), key)

    #     def siftDown(arr, start, end, key):
    #         if start >= end: return

    #         left = 2*start + 1
    #         right = 2*start + 2

    #         indices = [i for i in [start, left, right] if i < end]
    #         minIndex = min(indices, key=lambda i: key(arr[i]))
    #         if minIndex != start:
    #             arr[minIndex], arr[start] = arr[start], arr[minIndex]
    #             siftDown(arr, minIndex, end, key)

    #     arr = [node for node in lists if node]
    #     end = len(arr)
    #     heapify(arr, lambda node: node.val)

    #     head = ListNode(None)
    #     node = head
    #     while end > 0:
    #         minNode = arr[0]
    #         if minNode.next:
    #             arr[0] = minNode.next
    #             siftDown(arr, 0, end, lambda node: node.val)
    #         else:
    #             arr[0] = arr[end - 1]
    #             end -= 1
    #             siftDown(arr, 0, end, lambda node: node.val)
    #         node.next = minNode
    #         node = node.next
            
    #     return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        Divide and Conquer
        m is the length of lists and n is the number of all nodes
        Time Complexity: O(nlog(m))
        Space Complexity: O(m)
        '''
        def merge(lists: List[ListNode]) -> ListNode:
            if not lists: return None

            size = 1
            while size < len(lists):
                for i in range(0, len(lists), size * 2):
                    if i + size < len(lists):
                        lists[i] = mergeTwoLists(lists[i], lists[i + size])
                size *= 2

            return lists[0]

        def mergeTwoLists(node1: ListNode, node2: ListNode) -> ListNode:
            head = ListNode(None)
            curr = head

            while node1 and node2:
                if node1.val <= node2.val:
                    curr.next = node1
                    curr = curr.next
                    node1 = node1.next
                else:
                    curr.next = node2
                    curr = curr.next
                    node2 = node2.next

            for node in [node for node in (node1, node2) if node]:
                while node:
                    curr.next = node
                    curr = curr.next
                    node = node.next

            return head.next
            
        return merge(lists)


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

    # a = ListNode(1)
    # b = ListNode(0)
    # print(s.mergeKLists([a, b]))


if __name__ == '__main__':
    main()