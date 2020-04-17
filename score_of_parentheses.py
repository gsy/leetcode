# -*- coding: utf-8 -*-


class Solution:
    def scoreOfParentheses(self, string):
        length = len(string)
        if length == 0:
            return 0

        stack, scores, result = [], [], 0
        for index, char in enumerate(string):
            if index == 0:
                stack.push(char)
            else:
                if char == '(':
                    stack.push(char)
                elif char == ')':
                    if result
