from typing import List, Tuple
import unittest

class Solution(unittest.TestCase):
    #  def missingRanges(self, nums: List[int], low: int, high: int) -> List[Tuple[int, int]]:
        #  '''
        #  Time Complexity: O(n log n)
        #  Space Complexity: O(n)
        #  '''
        #  if not nums:
            #  return [(low, high)]

        #  nums += [low - 1, high + 1]
        #  nums.sort()

        #  ranges = []

        #  for i in range(len(nums) - 1):
            #  if nums[i] < nums[i + 1] - 1:
                #  ranges.append((nums[i] + 1, nums[i + 1] - 1))

        #  return ranges

    def missingRanges(self, nums: List[int], low: int, high: int) -> List[Tuple[int, int]]:
        '''
        Time Complexity: O(m)
        Space Complexity: O(n)
        '''
        s = set(nums)
        s.add(low - 1)
        s.add(high + 1)

        start = None
        ranges = []

        for i in range(low, high + 2):
            prevFound = i - 1 in s
            currFound = i in s

            if not currFound and prevFound:
                start = i
            elif currFound and not prevFound:
                ranges.append((start, i - 1))
            
        return ranges

    def test_1(self):
        self.assertEquals(self.missingRanges([1, 3, 5, 10], 1, 10), [(2, 2), (4, 4), (6, 9)])

    def test_2(self):
        self.assertEquals(self.missingRanges([2, 3, 5, 9], 1, 10), [(1, 1), (4, 4), (6, 8), (10, 10)])

    def test_3(self):
        self.assertEquals(self.missingRanges([1, 2, 3, 4, 5, 9], 1, 10), [(6, 8), (10, 10)])

    def test_4(self):
        self.assertEquals(self.missingRanges([], 1, 10), [(1, 10)])

    def test_5(self):
        self.assertEquals(self.missingRanges([5, 3, 1, 8], 1, 10), [(2, 2), (4, 4), (6, 7), (9, 10)])


def main():
    unittest.main()

if __name__ == '__main__':
    main()
