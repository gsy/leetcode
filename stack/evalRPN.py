#!/usr/bin/env python3

class Solution:
    def calculate(self, operator, a, b):
        a = int(a)
        b = int(b)
        # print(f"{a} {operator} {b}")
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        else:
            if abs(a) < abs(b):
                return 0
            return int(a / b)

    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                operator  = token
                b = stack.pop(-1)
                a = stack.pop(-1)
                tmp = self.calculate(operator, a, b)
                stack.append(tmp)
            else:
                stack.append(token)

        print(stack)
        return int(stack.pop())
