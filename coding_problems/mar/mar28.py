from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Set and tuples
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        '''
        nums.sort()
        completed = set()
        result = set()
        for i in range(len(nums) - 2):
            target = -nums[i]
            if target not in completed:
                completed.add(target)
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[j] + nums[k] < target:
                        j += 1
                    elif nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        result.add((nums[i], nums[j], nums[k]))
                        j += 1

        return result

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     '''
    #     No tuples
    #     Time Complexity: O(n^2)
    #     Space Complexity: O(n)
    #     '''
    #     d = {}
    #     for n in nums:
    #         if n not in d:
    #             d[n] = 0
    #         d[n] += 1

    #     nums = sorted(d.keys())
    #     result = []
    #     for i in range(len(nums)):
    #         target = -nums[i]
    #         j, k = i, len(nums) - 1

    #         while j <= k:
    #             if nums[j] + nums[k] < target:
    #                 j += 1
    #             elif nums[j] + nums[k] > target:
    #                 k -= 1
    #             else:
    #                 append = True
    #                 for index in (i, j, k):
    #                     d[nums[index]] -= 1
    #                     if d[nums[index]] < 0:
    #                         append = False

    #                 if append:
    #                     result.append([nums[i], nums[j], nums[k]])

    #                 for index in (i, j, k):
    #                     d[nums[index]] += 1

    #                 j += 1

    #     return result


def main():
    s = Solution()

    nums = [0, -1, 2, -3, 1]
    print(s.threeSum(nums))

    nums = [-1, 0, 1, 2, -1, 4]
    print(s.threeSum(nums))

if __name__ == '__main__':
    main()