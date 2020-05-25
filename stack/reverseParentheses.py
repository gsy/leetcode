#!/usr/bin/env python3

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        helper = []
        for char in s:
            if char == ")":
                count = 0
                while len(stack) > 0:
                    last = stack.pop(-1)
                    if last == "(":
                        break
                    else:
                        helper.append(last)
                        count = count + 1

                for i in range(count):
                    stack.append(helper.pop(0))
            else:
                stack.append(char)

        return "".join(stack)
