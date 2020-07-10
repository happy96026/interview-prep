import unittest
from typing import List

class Kadane(unittest.TestCase):
    def kadane(self, nums: List[int]) -> int:
        s = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            s += nums[i]
            maxSum = max(maxSum, s)
            if s < 0:
                s = 0

        return maxSum

    def test_1(self):
        self.assertEqual(self.kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
