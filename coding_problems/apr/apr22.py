import math

class Solution:
    # def findMinMax(self, nums):
    #     '''
    #     Worst Case: 2n - 3
    #     '''
    #     _min = nums[0]
    #     _max = nums[0]

    #     if nums[0] > nums[1]:
    #         _max = nums[0]
    #         _min = nums[1]
    #     else:
    #         _min = nums[0]
    #         _max = nums[1]

    #     for i in range(2, len(nums)):
    #         if nums[i] >= _max:
    #             _max = nums[i]
    #         elif nums[i] < _min:
    #             _min = nums[i]

    #     return (_min, _max)

    # def findMinMax(self, nums):
    #     '''
    #     Recursive
    #     Even: 1.5n - 2
    #     Odd: 1.5n
    #     '''
    #     def findMinMax(lo, hi):
    #         if hi - lo == 0:
    #             return (nums[lo], nums[lo])
    #         elif hi - lo == 1:
    #             return (nums[lo], nums[hi]) if nums[lo] < nums[hi] else (nums[hi], nums[lo])
    #         else:
    #             mid = (lo + hi) // 2
    #             left = findMinMax(lo, mid)
    #             right = findMinMax(mid + 1, hi)
    #             return (
    #                 left[0] if left[0] < right[0] else right[0],
    #                 left[1] if left[1] > right[1] else right[1]
    #             )

    #     return findMinMax(0, len(nums) - 1)

    def findMinMax(self, nums):
        '''
        Iterative
        Even: 1.5n - 2
        Odd: 1.5n
        '''
        i = 2
        if nums[0] < nums[1]:
            _min = nums[0]
            _max = nums[1]
        else:
            _min = nums[1]
            _max = nums[0]

        while i < len(nums):
            if i + 1 < len(nums):
                if nums[i] < nums[i + 1]:
                    lMin = nums[i]
                    lMax = nums[i + 1]
                else:
                    lMin = nums[i + 1]
                    lMax = nums[i]
                
                if lMin < _min:
                    _min = lMin
                if lMax > _max:
                    _max = lMax
            else:
                if nums[i] <= _min:
                    _min = nums[i]
                elif _max > nums[i]:
                    _max = nums[i]

            i += 2
        
        return (_min, _max)


def main():
    s = Solution()
    print(s.findMinMax([3, 5, 1, 2, 4, 8]))
    print(s.findMinMax([3, -5, 1, 2, 4, 8]))

if __name__ == '__main__':
    main()