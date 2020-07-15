import unittest
from typing import List

class Solution(unittest.TestCase):
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = []
        board = []
        rowSet = set()
        colSet = set()
        diag1Set = set()
        diag2Set = set()

        def search(i: int = 0):
            if i == n:
                solution.append([s for s in board])
            else:
                for j in range(n):
                    row = i
                    col = j
                    diag1 = i - j
                    diag2 = i + j
                    if row not in rowSet and col not in colSet and diag1 not in diag1Set and diag2 not in diag2Set:
                        boardRow = ['.'] * n
                        boardRow[j] = 'Q'

                        board.append(''.join(boardRow))
                        rowSet.add(row)
                        colSet.add(col)
                        diag1Set.add(diag1)
                        diag2Set.add(diag2)

                        search(i + 1)

                        board.pop()
                        rowSet.remove(row)
                        colSet.remove(col)
                        diag1Set.remove(diag1)
                        diag2Set.remove(diag2)

        search()
        return solution


    def test_1(self):
        result = self.solveNQueens(4)
        solution = [
            [
                '.Q..',
                '...Q',
                'Q...',
                '..Q.'
            ],
            [
                '..Q.',
                'Q...',
                '...Q',
                '.Q..'
            ]
        ]
        self.assertTrue(all(result[i][j] == solution[i][j] for i in range(max(len(result), len(solution))) for j in range(4)))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
