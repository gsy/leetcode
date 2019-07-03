# -*- coding: utf-8 -*-


class Solution:
    def add(self, a, b):
        return int(a) + int(b)

    def minus(self, a, b):
        return int(a) - int(b)

    def noop(self):
        pass

    def calculate(self, s: str) -> int:
        s = s.replace("(", " ( ")
        s = s.replace(")", " ) ")
        s = s.replace("-", " - ")
        s = s.replace("+", " + ")
        result = 0
        operator = self.add
        tokens = s.split(" ")
        operators = []
        numbers = []
        result = 0
        parentheses = 0

        for token in tokens:
            if token in (" ", ""):
                continue
            if token == "+":
                operators.append(self.add)
            elif token == "-":
                operators.append(self.minus)
            elif token == "(":
                # 分层
                operators.append("(")
                numbers.append(None)
            elif token == ")":
                # print("parenthese", operators, numbers)
                operators.pop()
                numbers.pop(-2)
            else:
                numbers.append(int(token))

            self.do_reduce_stack(operators, numbers)
            # print(operators, numbers)

        return numbers[0]

    def do_reduce_stack(self, operators, numbers):
        while len(operators) > 0:
            if len(numbers) < 2:
                break

            if operators[-1] in (self.add, self.minus) and numbers[-1] is not None and numbers[-2] is not None:
                operator = operators.pop()
                a = numbers.pop()
                b = numbers.pop()
                tmp = operator(b, a)
                numbers.append(tmp)
            else:
                break
