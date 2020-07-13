import unittest
from typing import List
from collections import Counter

class Solution(unittest.TestCase):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        _max = noMax = 0

        for v in counter.values():
            if v > _max:
                _max = v
                noMax = 1
            elif v == _max:
                noMax += 1

        return max(len(tasks), (_max - 1) * (n - noMax + 1) + _max * noMax)


    def test_1(self):
        self.assertEqual(self.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2), 8)

    def test_2(self):
        self.assertEqual(self.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 0), 6)

    def test_3(self):
        self.assertEqual(self.leastInterval(['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2), 16)

    def test_4(self):
        self.assertEqual(self.leastInterval([], 0), 0)

    def test_5(self):
        self.assertEqual(self.leastInterval(['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'], 2), 9)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
