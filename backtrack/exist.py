class Solution:
    def neighbor(self, location1, location2):
        x1, y1 = location1
        x2, y2 = location2

        if (x1 == x2 and abs(y1 - y2) == 1) or ((y1 == y2) and abs(x1 - x2) == 1):
            return True

    def backtrack(self, board, chars, word, used):
        for i, char in enumerate(word):
            if char not in chars:
                return False

            candidates = chars[char]
            # print(char, candidates)
            for candidate in candidates:
                if candidate not in used and (len(used) == 0 or self.neighbor(candidate, used[-1])):
                    used.append(candidate)
                    # print(used)
                    # word 要往下？
                    done = self.backtrack(board, chars, word[i+1:], used)
                    if done:
                        return True
                    used.pop(-1)
            return False
        return True

    def exist(self, board, word):
        nRows = len(board)
        nCols = len(board[0])

        chars = {}
        for i in range(nRows):
            for j in range(nCols):
                char = board[i][j]
                if char in chars:
                    ls = chars[char]
                    ls.append((i, j))
                else:
                    chars[char] = [(i, j)]

        last_word = []
        result = self.backtrack(board, chars, word, last_word)
        return result
