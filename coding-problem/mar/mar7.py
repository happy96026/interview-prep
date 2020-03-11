from typing import List
import math

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.mergeSortBottomUp(nums)
        return nums[-k]

    # O(n^2)
    def insertionSort(self, nums):
        for j in range(1, len(nums)):
            for i in range(j, 0, -1):
                if nums[i] < nums[i - 1]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
                else:
                    break

    # O(n^2)
    def bubbleSort(self, nums):
        for j in range(len(nums) - 1):
            for i in range(len(nums) - j - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

    # O(n^2)
    def selectionSort(self, nums):
        for i in range(len(nums) - 1):
            minIndex = i
            for j in range(i + 1, len(nums)):
                minIndex = min(minIndex, j, key=lambda x: nums[x])
            if i != minIndex:
                nums[i], nums[minIndex] = nums[minIndex] , nums[i]

    # O(n log n)
    def quickSortLomuto(self, nums):
        def partition(nums, left, right):
            pivot = nums[right]
            i = left
            for j in range(left, right + 1):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]

            return i

        def quickSortRecursive(nums, left, right):
            if left < right:
                p = partition(nums, left, right)
                quickSortRecursive(nums, left, p - 1)
                quickSortRecursive(nums, p + 1, right)

        quickSortRecursive(nums, 0, len(nums) - 1)

    # O(n log n)
    def quickSortHoare(self, nums):
        def partition(nums, left, right):
            pivot = nums[(left + right) // 2]
            i, j = left, right
            while True:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1

        def quickSortRecursive(nums, left, right):
            if left < right:
                p = partition(nums, left, right)
                quickSortRecursive(nums, left, p)
                quickSortRecursive(nums, p + 1, right)

        quickSortRecursive(nums, 0, len(nums) - 1)

    # O(n log n)
    # left is inclusive, right is exclusive
    def mergeSortTopDown(self, nums):
        def merge(nums, left, mid, right):
            i, j = left, mid
            mergedList = []
            for _ in range(left, right):
                if j >= right or (i < mid and nums[i] < nums[j]):
                    mergedList.append(nums[i])
                    i += 1
                else:
                    mergedList.append(nums[j])
                    j += 1

            for i in range(len(mergedList)):
                nums[left + i] = mergedList[i]

        def mergeSortRecursive(nums, left, right):
            if right - left > 1:
                mid = (left + right) // 2
                mergeSortRecursive(nums, left, mid)
                mergeSortRecursive(nums, mid, right)
                merge(nums, left, mid, right)
        
        mergeSortRecursive(nums, 0, len(nums))

    # O(n log n)
    # left is inclusive, right is exclusive
    def mergeSortBottomUp(self, nums):
        def merge(nums, left, mid, right):
            i, j = left, mid
            mergedList = []
            for _ in range(left, right):
                if j >= right or (i < mid and nums[i] < nums[j]):
                    mergedList.append(nums[i])
                    i += 1
                else:
                    mergedList.append(nums[j])
                    j += 1
            
            for i in range(len(mergedList)):
                nums[left + i] = mergedList[i]

        size = 1
        while size < len(nums):
            left = 0
            while left < len(nums):
                right = min(len(nums), left + 2 * size)
                mid = min(len(nums), left + size)
                merge(nums, left, mid, right)
                left += 2 * size 
            size *= 2

    def heapSort(self, nums):
        pass


def main():
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(s.findKthLargest([3, 5, 2, 4, 6, 8], 3))
    # print(s.findKthLargest([1, 2, 3], 0))
    # print(s.findKthLargest([1, 2], 0))
    # print(s.findKthLargest([2, 1], 0))
    # print(s.findKthLargest([], 0))

if __name__ == '__main__':
    main()