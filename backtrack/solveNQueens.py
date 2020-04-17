class Solution:
    def printBoard(self, board, rows, columns):
        for i in range(rows):
            print(" ".join(board[i]))
        print()

    def fit(self, board, row, column, N):
        for i in range(N):
            for j in range(N):
                if i == row and j == column:
                    continue

                if board[i][j] == 'Q':
                    if i == row or j == column or abs(i-row) == abs(j-column):
                        return False
        return True

    def backtrack(self, board, N, row, result):
        if row == N:
            # self.printBoard(board, N, N)
            result.append([''.join(board[i]) for i in range(N)])
            return

        for j in range(N):
            if self.fit(board, row, j, N):
                board[row][j] = 'Q'
                self.backtrack(board, N, row+1, result)
                board[row][j] = '.'
        return

    def solveNQueens(self, n):
        board = [['.'] * n for i in range(n)]
        result = []
        self.backtrack(board, n, 0, result)
        return result
