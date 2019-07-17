# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.states = ['init', 'letter', 'dot', 'star']

    def isMatch(self, string, pattern):
        state = 'init'

        if pattern == '':
            return string == ''

        i, j, len_pattern, len_string = 0, 0, len(pattern), len(string)
        while i < len_pattern and j < len_string:
            p = pattern[i]
            s = string[j]

            if p.isalpha():
                state == 'letter'
                if s != p:
                    return False
                else:
                    i, j = i + 1, j + 1
                    continue
            elif p == '.':
                state = 'dot'
                i, j = i + 1, j + 1
                continue
            elif p == '*':
                state = 'star'
