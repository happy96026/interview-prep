from typing import List

class Solution:
    def fixedPoint(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > mid:
                hi = mid - 1
            elif nums[mid] < mid:
                lo = mid + 1
            else:
                return mid

        return None


def main():
    s = Solution()
    print(s.fixedPoint([-5, 1, 3, 4]))

if __name__ == '__main__':
    main()
