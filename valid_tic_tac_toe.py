# -*- coding: utf-8 -*-


class Solution:
    def same_in_line(self, line):
        return line == "XXX" or line == "OOO"

    def validTicTacToe(self, board):
        first, second, finished = 0, 0, False

        for i in range(len(board)):
            row = board[i]
            if len(row) > 3:
                return False

            for j, char in enumerate(row):
                if char == "X":
                    first = first + 1
                elif char == "O":
                    second = second + 1

                # 怎么判断有没有游戏结束？跟递归有什么关系？
                if j == 2:
                    if self.same_in_line(row):
                        finished = True
                        continue

                if i == 2:
                    column = "".join([board[m][j] for m in range(3)])
                    print("column:", column)
                    if self.same_in_line(column):
                        finished = True
                        continue
                if i == 2 and j == 0:
                    line = board[0][2] + board[1][1] + board[2][0]
                    if self.same_in_line(line):
                        finished = True
                        continue

                elif i == 2 and j == 2:
                    line = board[0][0] + board[1][1] + board[2][2]
                    if self.same_in_line(line):
                        finished = True
                        continue

        return first == second or first == second + 1


if __name__ == '__main__':
    s = Solution()
    board = ["O  ", "   ", "   "]
    r = s.validTicTacToe(board)
    assert r is False

    board = ["XOX", " X ", "   "]
    r = s.validTicTacToe(board)
    assert r is False

    board = ["XXX", "   ", "OOO"]
    r = s.validTicTacToe(board)
    assert r is False

    board = ["XOX", "O O", "XOX"]
    r = s.validTicTacToe(board)
    assert r is True

    board = ["XO ", "XO ", "X  "]
    r = s.validTicTacToe(board)
    assert r is True

    board = ["XXX", "OOX", "OOX"]
    r = s.validTicTacToe(board)
    assert r is True
