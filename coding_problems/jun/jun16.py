from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        arr = [0] * len(obstacleGrid[0])
        arr[0] = 1

        for row in obstacleGrid:
            if row[0]:
                arr[0] = 0
            for j in range(1, len(row)):
                arr[j] = 0 if row[j] else arr[j - 1] + arr[j]

        return arr[len(obstacleGrid[0]) - 1]


def main():
    s = Solution()

    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(s.uniquePathsWithObstacles(grid))

    grid = [
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0]
    ]
    print(s.uniquePathsWithObstacles(grid))

if __name__ == '__main__':
    main()
