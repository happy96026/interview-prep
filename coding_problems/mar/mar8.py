from typing import List

# Simulation
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix:
#             return matrix
#         elif len(matrix) == 1:
#             return matrix[0]

#         traversals = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
#         i = row = col = 0
#         result = []

#         for _ in range(len(matrix) * len(matrix[0])):
#             result.append(matrix[row][col])
#             visited[row][col] = True
#             row, col = row + traversals[i][0], col + traversals[i][1]
#             if row == -1 or row == len(matrix) or col == -1 or col == len(matrix[0]) or visited[row][col]:
#                 row, col = row - traversals[i][0], col - traversals[i][1]
#                 i = (i + 1) % len(traversals)
#                 row, col = row + traversals[i][0], col + traversals[i][1]

#         return result

# Strip Matrix
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         result = []
#         while matrix:
#             result += matrix[0]
#             matrix = list(zip(*matrix[1:]))[::-1]

#         return result

# Layer by Layer
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix

        def getValue(r1, c1, r2, c2):
            for col in range(c1, c2 + 1):
                yield matrix[r1][col]
            for row in range(r1 + 1, r2 + 1):
                yield matrix[row][c2]
            if r1 < r2:
                for col in range(c2 - 1, c1 - 1, -1):
                    yield matrix[r2][col]
            if c1 < c2:
                for row in range(r2 - 1, r1, -1):
                    yield matrix[row][c1]

        r1 = c1 = 0
        r2, c2 = len(matrix) - 1, len(matrix[0]) - 1
        result = []
        while r1 <= r2 and c1 <= c2:
            for x in getValue(r1, c1, r2, c2):
                result.append(x)
            r1, c1 = r1 + 1, c1 + 1
            r2, c2 = r2 - 1, c2 - 1

        return result

def main():
    s = Solution()
    grid = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    print(s.spiralOrder(grid))
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(s.spiralOrder(grid))
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(s.spiralOrder(grid))
    grid = [
        [7]
    ]
    print(s.spiralOrder(grid))

if __name__ == '__main__':
    main()