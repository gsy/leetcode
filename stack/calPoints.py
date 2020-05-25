#!/usr/bin/env python3

class Solution:
    def calPoints(self, ops):
        helper = []
        stack = []

        result = 0
        for char in ops:
            if char == "+":
                stack.append(stack[-1] + stack[-2])
            elif char == "D":
                stack.append(stack[-1] * 2)
            elif char == "C":
                stack.pop(-1)
            else:
                stack.append(int(char))

        # print(stack)
        return sum(stack)
