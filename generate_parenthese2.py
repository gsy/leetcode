# -*- coding: utf-8 -*-


class Solution:
    def generateParenthesis(self, n):
        if n == 1:
            return ["()"]
        elif n == 2:
            return ["()()", "(())"]
        else:
            result = set()
            for parenthesis in self.generateParenthesis(n-1):
                result.add("({})".format(parenthesis))
                result.add("(){}".format(parenthesis))
                result.add("{}()".format(parenthesis))
            return list(result)


if __name__ == '__main__':
    s = Solution()
    r = s.generateParenthesis(3)
    print(r)

    r = s.generateParenthesis(4)
    print(r, len(r))
    assert len(r) == 14
