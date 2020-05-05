from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for n in nums:
            if n - 1 not in nums:
                up = n + 1
                while up in nums:
                    up += 1
                
                longest = max(longest, up - n)

        return longest


def main():
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))

if __name__ == '__main__':
    main()