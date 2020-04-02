import heapq

class MedianFinder:
    def __init__(self):
        """
        Two Heap (min and max)
        """ 
        self.minHeap = []
        self.maxHeap = []

    # def addNum(self, num: int) -> None:
    #     '''
    #     Time Complexity: O(log n)
    #     Space Complexity: O(1)
    #     '''
    #     if self.maxHeap and num < -self.maxHeap[0]:
    #         heap1, heap2 = (self.maxHeap, self.minHeap)
    #     else:
    #         heap1, heap2 = (self.minHeap, self.maxHeap)

    #     num *= -1 if heap1 is self.maxHeap else 1
    #     if len(heap1) > len(heap2):
    #         popped = heapq.heappushpop(heap1, num) * -1
    #         heapq.heappush(heap2, popped)
    #     else:
    #         heapq.heappush(heap1, num)

    # def findMedian(self) -> float:
    #     '''
    #     Time Complexity: O(1)
    #     Space Complexity: O(1)
    #     '''
    #     if not (self.minHeap or self.maxHeap):
    #         raise IndexError('No values have been added.')

    #     if len(self.minHeap) < len(self.maxHeap):
    #         return -self.maxHeap[0]
    #     elif len(self.minHeap) > len(self.maxHeap):
    #         return self.minHeap[0]
    #     else:
    #         return (self.minHeap[0] + -self.maxHeap[0]) / 2

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if not (self.minHeap or self.maxHeap):
            raise IndexError('No values have been added.')
    
        return -self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) else (self.minHeap[0] - self.maxHeap[0]) / 2

        
def main():
    s = MedianFinder()

    s.addNum(2)
    print(s.findMedian())

    s.addNum(1)
    print(s.findMedian())

    s.addNum(4)
    print(s.findMedian())

    s.addNum(7)
    print(s.findMedian())

    s.addNum(2)
    print(s.findMedian())

    s.addNum(0)
    print(s.findMedian())

    s.addNum(5)
    print(s.findMedian())

if __name__ == '__main__':
    main()