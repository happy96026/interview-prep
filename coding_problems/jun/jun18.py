from typing import List

class Solution:
    def closestPoints(self, points: List[List[int]], k: int, p: List[int]) -> List[List[int]]:
        dists = [((p[0] - points[i][0]) ** 2 + (p[1] - points[i][1]) ** 2, i) for i in range(len(points))]
        lo = 0
        hi = len(points) - 1
        while lo != k:
            pivot = dists[(lo + hi) // 2][0]
            i = lo
            j = hi
            while True:
                while dists[i][0] < pivot:
                    i += 1
                while dists[j][0] > pivot:
                    j -= 1
                if i >= j:
                    break
                dists[i], dists[j] = dists[j], dists[i]
                i += 1
                j -= 1

            if j < k:
                lo = j + 1
            else:
                hi = j

        return [points[dists[i][1]] for i in range(k)]


def main():
    s = Solution()
    print(s.closestPoints(
        [
            [0, 0],
            [1, 1],
            [2, 2],
            [3, 3]
        ],
        2,
        [0, 2]
    ))

if __name__ == '__main__':
    main()
