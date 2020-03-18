import math
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        smallest = _sum = 0
        largest = -math.inf

        for n in nums:
            _sum += n
            largest = max(largest, _sum - smallest)
            smallest = min(smallest, _sum)

        return largest


def main():
    s = Solution()
    print(s.maxSubArray([1,2,-4,2,3,-6,32,2,1,2,-6,-6,2]))

if __name__ == '__main__':
    main()