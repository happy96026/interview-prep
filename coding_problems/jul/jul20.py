from typing import List
import unittest

class Solution(unittest.TestCase):
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def calcDistSquared(point):
            return point[0] ** 2 + point[1] ** 2

        lo = 0
        hi = len(points) - 1

        while lo != K:
            i = lo
            j = hi
            pivot = calcDistSquared(points[(lo + hi) // 2])

            while True:
                while calcDistSquared(points[i]) < pivot:
                    i += 1
                while calcDistSquared(points[j]) > pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]
                i += 1
                j -= 1

            if j < K:
                lo = j + 1
            else:
                hi = j

        return points[:K]

    def test_1(self):
        solutionSet = set([(1, 2), (0, 0)])
        resultSet = set(self.kClosest([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))

        n = 0
        for t in resultSet:
            if t in solutionSet:
                n += 1

        self.assertEqual(n, len(solutionSet))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

