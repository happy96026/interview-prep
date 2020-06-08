from typing import List
import math

class Solution:
    def minWindowToSort(self, nums: List[int]) -> List[int]:
        _min = math.inf
        _max = -math.inf
        lo = 0
        hi = 0

        for i, n in enumerate(nums):
            if n > _max:
                _max = n
            else:
                hi = i

        for i in reversed(range(len(nums))):
            n = nums[i]
            if n < _min:
                _min = n
            else:
                lo = i

        return [lo, hi]




def main():
    s = Solution()
    print(s.minWindowToSort([2, 4, 7, 5, 6, 8, 9]))

if __name__ == '__main__':
    main()
