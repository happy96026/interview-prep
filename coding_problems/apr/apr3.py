from typing import List, Tuple
import heapq

class Solution:
    def meetingRooms(self, intervals: List[Tuple[int, int]]) -> int:
        '''
        Heap
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        '''
        intervals.sort(key=lambda t: t[0])
        rooms = 0
        heap = []
        for start, end in intervals:
            heapq.heappush(heap, end)
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            rooms = max(rooms, len(heap))

        return rooms


def main():
    s = Solution()
    print(s.meetingRooms([(30, 75), (0, 50), (60, 150)]))
    print(s.meetingRooms([(2, 15), (36, 45), (9, 25), (16, 23), (4, 9)]))

if __name__ == '__main__':
    main()