# -*- coding: utf-8 -*-


class Solution:
    def rows(self, char):
        char = char.lower()
        if char in ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'):
            return 1
        elif char in ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'):
            return 2
        elif char in ('z', 'x', 'c', 'v', 'b', 'n', 'm'):
            return 3

    def same_row(self, word):
        if len(word) == 0:
            return True

        row = None
        for char in word:
            current = self.rows(char)
            if row is None:
                row = current
            elif row != current:
                return False

        return True

    def findWords(self, words):
        result = []
        for word in words:
            if self.same_row(word):
                result.append(word)
        return result
