from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


def main():
    s = Solution()
    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    s.moveZeroes(nums)
    print(nums)

if __name__ == '__main__':
    main()