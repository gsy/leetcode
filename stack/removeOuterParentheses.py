#!/usr/bin/env python3

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        stack = []

        for i, char in enumerate(S):
            if len(stack) == 0 and char == "(":
                start = i

            stack.append(char)

            if stack[-1] == ")" and stack[-2] == "(":
                stack.pop(-1)
                stack.pop(-1)

            if len(stack) == 0:
                end = i
                # print(start, end)
                result = result + S[start+1: end]

        return result
