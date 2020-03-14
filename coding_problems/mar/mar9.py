from typing import List
import math

# O(n log n)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

# O(n)
# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         max0 = max1 = max2 = -math.inf
#         min0 = min1 = math.inf
#         for n in nums:
#             if n < min0:
#                 min1 = min0
#                 min0 = n
#             elif n < min1:
#                 min1 = n

#             if n > max2:
#                 max0 = max1
#                 max1 = max2
#                 max2 = n
#             elif n > max1:
#                 max0 = max1
#                 max1 = n
#             elif n > max0:
#                 max0 = n

#         return max(max0 * max1 * max2, min0 * min1 * max2)

def main():
    s = Solution()
    print(s.maximumProduct([-4, -4, 2, 8]))
    print(s.maximumProduct([1, 2, 3]))
    print(s.maximumProduct([1, 2, 3, 4]))
    print(s.maximumProduct([-2, -1, -3, 0]))

if __name__ == '__main__':
    main()