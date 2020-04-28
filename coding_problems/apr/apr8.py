from typing import List
import math
import sys

sys.setrecursionlimit(10**6)

class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     '''
    #     Time Complexity: O(n^2)
    #     Space Complexity: O(n)
    #     '''
    #     arr = [0] * len(nums)
    #     maxLength = 0

    #     for j in range(len(nums)):
    #         length = 0
    #         for i in range(j):
    #             if nums[i] < nums[j]:
    #                 length = max(length, arr[i])

    #         arr[j] = length + 1
    #         maxLength = max(maxLength, arr[j])

    #     return maxLength

    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Binary Search
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        '''
        def binarySearch(arr, target):
            i, j = 0, len(arr) - 1
            while i < j:
                mid = (i + j) // 2
                if arr[mid] < target:
                    i = mid + 1
                else:
                    j = mid

            return i

        if not nums:
            return 0

        arr = [math.inf]
        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                i = binarySearch(arr, n)
                arr[i] = n
            
        return len(arr)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     '''
    #     Brute Force
    #     Time Complexity: O(2^n)
    #     Space Complexity: O(n^2)
    #     '''
    #     def lengthOfLIS(i = 0, prev = -math.inf):
    #         if i == len(nums):
    #             return 0

    #         len1 = lengthOfLIS(i + 1, prev)
    #         len2 = 0

    #         if prev < nums[i]:
    #             len2 = lengthOfLIS(i + 1, nums[i]) + 1
            
    #         return max(len1, len2)
            
    #     return lengthOfLIS()

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     '''
    #     Memoization
    #     Time Complexity: O(n^2)
    #     Space Complexity: O(n^2)
    #     '''
    #     arr = [[-1] * len(nums) for _ in range(len(nums))]
    #     def lengthOfLIS(i = 0, prevIndex = -1):
    #         if i == len(nums):
    #             return 0

    #         if arr[i][prevIndex] < 0:
    #             len1 = lengthOfLIS(i + 1, prevIndex)
    #             len2 = 0

    #             if prevIndex < 0 or nums[prevIndex] < nums[i]:
    #                 len2 = lengthOfLIS(i + 1, i) + 1
                
    #             arr[i][prevIndex] = max(len1, len2)

    #         return arr[i][prevIndex]
            
    #     return lengthOfLIS()


def main():
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
    print(s.lengthOfLIS([i for i in range(-1, -2501, -1)]))

if __name__ == '__main__':
    main()