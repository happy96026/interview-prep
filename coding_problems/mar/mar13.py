import math
from typing import List

class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     '''
    #     Best Time to Buy and Sell Stock

    #     Time Complexity: O(n)
    #     Space Complexity: O(1)
    #     '''
    #     smallest = _sum = 0
    #     largest = -math.inf

    #     for n in nums:
    #         _sum += n
    #         largest = max(largest, _sum - smallest)
    #         smallest = min(smallest, _sum)

    #     return largest

    # def maxSubArray(self, nums: List[int]) -> int:
    #     '''
    #     Dynamic Programming Recursive

    #     Time Complexity: O(n)
    #     Space Complexity: O(n)
    #     '''
    #     def d(i, store={0: nums[0]}):
    #         if i not in store:
    #             store[i] = max(nums[i], d(i - 1) + nums[i])
            
    #         return store[i]

    #     result = []
    #     for i in range(len(nums)):
    #         result.append(d(i))

    #     return max(result)

    # def maxSubArray(self, nums: List[int]) -> int:
    #     '''
    #     Dynamic Programming Iterative

    #     Time Complexity: O(n)
    #     Space Complexity: O(1)
    #     '''
    #     maxSum = -math.inf
    #     currSum = 0
    #     for i in range(len(nums)):
    #         currSum = max(currSum + nums[i], nums[i])
    #         maxSum = max(currSum, maxSum)

    #     return maxSum

    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Divide and Conquer

        Time Complexity: O(n log n)
        Space Complexity: O(log n)
        '''
        def maxSubArrayRecursive(nums, start, end):
            if end - start == 1:
                return nums[start]
            else:
                mid = (start + end) // 2

                ml = mr = -math.inf
                currSum = 0
                for i in reversed(range(start, mid)):
                    currSum += nums[i]
                    ml = max(ml, currSum)

                currSum = 0
                for i in range(mid, end):
                    currSum += nums[i]
                    mr = max(mr, currSum)

                return max(ml + mr, maxSubArrayRecursive(nums, start, mid), maxSubArrayRecursive(nums, mid, end))

        return maxSubArrayRecursive(nums, 0, len(nums))


def main():
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([-2, -3, -5, 1]))
    print(s.maxSubArray([1, -2, -3, -5]))
    print(s.maxSubArray([-2, -3, -5, -6]))
    print(s.maxSubArray([1,2,-4,2,3,-6,32,2,1,2,-6,-6,2]))

if __name__ == '__main__':
    main()