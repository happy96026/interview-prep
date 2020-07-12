import unittest
from typing import List

class Solution(unittest.TestCase):
    def numSquares(self, n: int, dp: List[int] = [0]) -> int:
        prevLen = len(dp)

        if prevLen < n + 1:
            dp += [n] * (n + 1 - prevLen)

        for i in range(1, int(n ** 0.5) + 1):
            s = i * i
            for j in range(max(s, prevLen), n + 1):
                dp[j] = min(dp[j], dp[j - s] + 1)

        return dp[n]

    def test_1(self):
        self.assertEqual(self.numSquares(13), 2)

    def test_2(self):
        self.assertEqual(self.numSquares(32), 2)

    def test_3(self):
        self.assertEqual(self.numSquares(25), 1)

    def test_4(self):
        self.assertEqual(self.numSquares(0), 0)

    def test_5(self):
        self.assertEqual(self.numSquares(12), 3)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
