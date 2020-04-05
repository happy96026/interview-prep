from typing import List
import math

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums

        arr = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            n = nums[i]
            rangeMin, rangeMax = arr[-1]

            if n > rangeMax + 1:
                arr[-1] = str(rangeMin) + ('->' + str(rangeMax) if rangeMax > rangeMin else '')
                arr.append([n, n])
            else:
                arr[-1][-1] = n

        rangeMin, rangeMax = arr[-1]
        arr[-1] = str(rangeMin) + ('->' + str(rangeMax) if rangeMax > rangeMin else '')

        return arr
        

def main():
    s = Solution()
    print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print(s.summaryRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))

if __name__ == '__main__':
    main()