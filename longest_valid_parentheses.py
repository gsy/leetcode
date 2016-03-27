__author__ = 'guang'

class Solution(object):
    def match(self, left, right):
        return left == '(' and right == ')'

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        >>> s = Solution()
        >>> s.longestValidParentheses("(")
        0
        >>> s.longestValidParentheses(")")
        0
        >>> s.longestValidParentheses("()")
        2
        >>> s.longestValidParentheses(")(")
        0
        >>> s.longestValidParentheses("((")
        0
        >>> s.longestValidParentheses("))")
        0
        >>> s.longestValidParentheses("(()")
        2
        >>> s.longestValidParentheses("(((")
        0
        >>> s.longestValidParentheses(")()())")
        4
        >>> s.longestValidParentheses(")))()")
        2
        >>> s.longestValidParentheses("(()(()()(")
        4
        >>> s.longestValidParentheses("")
        0
        >>> s.longestValidParentheses("((())))")
        6
        >>> s.longestValidParentheses("(())(())((()))")
        14

        # >>> s.longestValidParentheses("))(())(())((())))()((())()(()))())(((())))((())((((()()))()()((()())(()))))((((()()((())())())()))()))))(()))))()((())))())((()()))))(()))((((()(()))))(((((()(")
        # 68
        """
        if len(s) == 0:
            return 0

        total = len(s)
        result = [[0]*len(s)] * len(s)
        length = 1
        for i in range(0, total - length):
            j = i + length
            if self.match(s[i], s[j]):
                result[i][j] = 2
            else:
                result[i][j] = 0

        for length in range(2, total):
            for i in range(0, total - length):
                j = i + length
                if self.match(s[i], s[j]) and j - 1 > i + 1 and result[i+1][j-1] == (j-1) - (i+1) + 1:
                        result[i][j] = result[i+1][j-1] + 2
                else:
                    result[i][j] = max(result[i][j-1], result[i+1][j])

        return result[0][total-1]
