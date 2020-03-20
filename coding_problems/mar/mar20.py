from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Cycle Sort
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        i = 0
        while i < len(nums):
            n = nums[i]
            if 1 <= n <= len(nums) and n != i + 1 and nums[i] != nums[n - 1]:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
            else:
                i += 1
        
        i = 0
        while i < len(nums) and nums[i] == i + 1:
            i += 1

        return i + 1


def main():
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))
    print(s.firstMissingPositive([1, 2]))
    print(s.firstMissingPositive([1, 1]))

if __name__ == '__main__':
    main()