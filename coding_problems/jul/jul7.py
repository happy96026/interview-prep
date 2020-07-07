from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def main():
    s = Solution()

    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(m)
    print(m)

    m = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s.rotate(m)
    print(m)

    m = [
        [1],
    ]
    s.rotate(m)
    print(m)

    m = []
    s.rotate(m)
    print(m)

if __name__ == '__main__':
    main()
