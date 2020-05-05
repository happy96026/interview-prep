from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = { 0: -1 }
        s = 0
        for i, n in enumerate(nums):
            s += n
            d[s] = i
            if s - k in d:
                return nums[d[s - k] + 1:i + 1]


def main():
    s = Solution()
    print(s.subarraySum([1, 3, 2, 5, 7, 2], 14))

if __name__ == '__main__':
    main()