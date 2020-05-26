from typing import List
import heapq

class Solution:
    def sortPartiallySorted(self, nums: List[int], k: int) -> List[int]:
        heap = [nums[i] for i in range(k)]
        heapq.heapify(heap)

        sortedArr = []
        for i in range(k, len(nums)):
            sortedArr.append(heapq.heappushpop(heap, nums[i]))

        while heap:
            sortedArr.append(heapq.heappop(heap))

        return sortedArr


def main():
    s = Solution()
    print(s.sortPartiallySorted([3, 2, 6, 5, 4], 2))

if __name__ == '__main__':
    main()
