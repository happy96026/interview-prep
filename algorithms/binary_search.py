import unittest
from typing import List

class BinarySearch(unittest.TestCase):
    def searchLeft(self, target, nums: List[int]):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def searchRight(self, target, nums: List[int]):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2

    def test_1(self):
        self.assertEquals(self.searchLeft(3, [1, 3, 3, 3, 5]), 1)

    def test_2(self):
        self.assertEquals(self.searchRight(4, [1, 3, 3, 3, 5]), 3)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
