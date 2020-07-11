from typing import List
import unittest

class Solution(unittest.TestCase):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != '.':
                    boxNo = i // 3 * 3 + j // 3
                    if n in rows[i] or n in cols[j] or n in boxes[boxNo]:
                        return False
                    rows[i].add(n)
                    cols[j].add(n)
                    boxes[boxNo].add(n)
        return True

    def test_1(self):
        self.assertTrue(
            self.isValidSudoku([
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ])
        )

    def test_2(self):
        self.assertFalse(
            self.isValidSudoku([
                ["8","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ])
        )


def main():
    unittest.main()

if __name__ == '__main__':
    main()
