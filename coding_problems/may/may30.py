from typing import List
import heapq
import math

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        buildings = [(-z, x, y) for x, y, z in buildings] + [(0, math.inf, math.inf)]

        heap = []
        skylines = []

        for building in buildings:
            while heap and heap[0][2] < building[1]:
                popped = heapq.heappop(heap)
                while heap and popped[2] >= heap[0][2]:
                    heapq.heappop(heap)

                if not heap:
                    skylines.append([popped[2], 0])
                elif popped[0] < heap[0][0]:
                    skylines.append([popped[2], -heap[0][0]])

            if not skylines:
                skylines.append([building[1], -building[0]])
            elif -building[0] > skylines[-1][1]:
                if skylines[-1][0] == building[1]:
                    skylines[-1][1] = -building[0]
                else:
                    skylines.append([building[1], -building[0]])

            heapq.heappush(heap, building)

        return skylines


def main():
    s = Solution()
    print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    print(s.getSkyline([[2, 8, 3], [4, 6, 5]]))

if __name__ == '__main__':
    main()
