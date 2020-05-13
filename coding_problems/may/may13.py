class TicTacToe:
    def __init__(self, n):
        self.board = [[''] * n for _ in range(n)]
        self.size = n
    
    def move(self, row, col, player):
        c = 'X' if player == 1 else 'O'

        self.board[row][col] = c

        if self.checkRow(row, c):
            return player

        if self.checkCol(col, c):
            return player

        if row == col and self.checkDiag1(c):
            return player

        if row + col == self.size - 1 and self.checkDiag2(c):
            return player

        return 0

    def checkRow(self, row, c):
        for i in range(self.size):
            if self.board[row][i] != c:
                return False

        return True

    def checkCol(self, col, c):
        for i in range(self.size):
            if self.board[i][col] != c:
                return False

        return True

    def checkDiag1(self, c):
        for i in range(self.size):
            if self.board[i][i] != c:
                return False

        return True

    def checkDiag2(self, c):
        for i in range(self.size):
            if self.board[i][self.size - 1 - i] != c:
                return False

        return True


def main():
    board = TicTacToe(3)
    print(board.move(0, 0, 1))
    print(board.move(0, 2, 2))
    print(board.move(2, 2, 1))
    print(board.move(1, 1, 2))
    print(board.move(2, 0, 1))
    print(board.move(1, 0, 2))
    print(board.move(2, 1, 1))

if __name__ == '__main__':
    main()