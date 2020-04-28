from typing import List
import math

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = right = 0

        maxVal = -math.inf
        for i in range(len(nums)):
            if maxVal > nums[i]:
                right = i
            else:
                maxVal = nums[i]

        minVal = math.inf
        for i in reversed(range(len(nums))):
            if minVal < nums[i]:
                left = i
            else:
                minVal = nums[i]

        return 0 if left == right else right - left + 1


def main():
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(s.findUnsortedSubarray([1, 7, 9, 5, 7, 8, 10]))
    print(s.findUnsortedSubarray([1, 2, 3, 4]))

if __name__ == '__main__':
    main()