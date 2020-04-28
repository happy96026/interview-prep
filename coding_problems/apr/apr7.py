from typing import List

class Solution:
    # def intersection(self, nums1: List[int], num2: List[int]) -> List[int]:
    #     return list(set(nums1).intersection(set(num2)))

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)
        s1, s2 = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        s = set()
        for n in s1:
            if n in s2:
                s.add(n)

        return list(s)


def main():
    s = Solution()
    print(s.intersection([1, 2, 2, 1], [2, 2]))
    print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))

if __name__ == '__main__':
    main()