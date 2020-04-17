class Solution:
    def printBoard(self, board, rows, columns):
        for i in range(rows):
            print(" ".join(board[i]))
        print()

    def trySolveWith(self, c, board, rows, columns, row, column):
        # row
        for j, value in enumerate(board[row]):
            if board[row][j] == c and column != j:
                return False
        # column
        for i in range(rows):
            if board[i][column] == c and row != i:
                return False

        # 一个数字只能在 3*3中出现
        start_i = int(row / 3) * 3
        start_j = int(column / 3) * 3
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                if board[i][j] == c and i != row and j != column:
                    return False

        return True

    def recurse(self, board, rows, columns):

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == '.':
                    for c in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        fine = self.trySolveWith(c, board, rows, columns, i, j)
                        if fine:
                            board[i][j] = c
                            # self.printBoard(board, rows, columns)
                            done = self.recurse(board, rows, columns)
                            if done:
                                return True
                            else:
                                board[i][j] = '.'

                    # 所有的候选都不合适
                    board[i][j] = '.'
                    return False

        return True

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        columns = len(board[0])
        self.printBoard(board, rows, columns)
        self.recurse(board, rows, columns)
        self.printBoard(board, rows, columns)
