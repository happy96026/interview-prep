from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        result = []
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                result.append(i + 1)

        return result


def main():
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.findDisappearedNumbers([4, 5, 2, 6, 8, 2, 1, 5]))
    print(s.findDisappearedNumbers([4, 6, 2, 6, 7, 2, 1]))

if __name__ == '__main__':
    main()