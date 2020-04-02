from typing import List

class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     '''
    #     One-Pass
    #     Time Complexity: O(n)
    #     Space Complexity: O(1)
    #     '''
    #     i, j = 0, len(nums) - 1
    #     k = 0
    #     while k <= j:
    #         if nums[k] == 0:
    #             nums[i], nums[k] = nums[k], nums[i]
    #             i += 1
    #             k += 1
    #         elif nums[k] == 2:
    #             nums[j], nums[k] = nums[k], nums[j]
    #             j -= 1
    #         else:
    #             k += 1

    def sortColors(self, nums: List[int]) -> None:
        '''
        Two-Pass
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        _set = (0, 1, 2)
        d = { n: 0 for n in _set }
        for n in nums:
            d[n] += 1
        
        i = 0
        for n in _set:
            for _ in range(d[n]):
                nums[i] = n
                i += 1


def main():
    s = Solution()

    colors = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
    s.sortColors(colors)
    print(colors)

    colors = [2, 0, 2, 1, 1, 0]
    s.sortColors(colors)
    print(colors)


if __name__ == '__main__':
    main()