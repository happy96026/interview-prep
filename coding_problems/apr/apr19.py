from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currMax = newMax = 0
        for i in range(len(nums)):
            if currMax < i:
                jumps += 1
                currMax = newMax
            newMax = max(newMax, i + nums[i])

        return jumps


def main():
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
    print(s.jump([3, 2, 5, 1, 1, 9, 3, 4]))
    print(s.jump([0]))
    print(s.jump([2, 0]))

if __name__ == '__main__':
    main()