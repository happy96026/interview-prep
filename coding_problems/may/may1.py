from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def permute(level):
            if level == len(nums) - 1:
                permutations.append(nums[:])
            else:
                for i in range(level, len(nums)):
                    nums[level], nums[i] = nums[i], nums[level]
                    permute(level + 1)
                    nums[level], nums[i] = nums[i], nums[level]
                
        permute(0)

        return permutations



def main():
    s = Solution()
    print(s.permute([1, 2, 3]))

if __name__ == '__main__':
    main()