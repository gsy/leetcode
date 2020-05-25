#!/usr/bin/env python3

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []

        for char in S:
            if char == "(":
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    stack.append(char)

        return len(stack)
