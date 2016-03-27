__author__ = 'guang'

class Solution(object):
    def all_match(self, result, s, left, right):
        length = right - left + 1
        if length < 2:
            return False

        if s[left] == '(' and s[right] == ')':
            if result[left+1][right-1] == (right - 1) - (left + 1) + 1:
                return True

            for k in range(left+1, right-1):
                if result[left][k] == k - left + 1 and result[k+1][right] == right - (k+1) + 1:
                    return True

        return False

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
        >>> s.longestValidParentheses("")
        0

        >>> s.longestValidParentheses("((())))")
        6

        >>> s.longestValidParentheses("(())(())((()))")
        14

        >>> s.longestValidParentheses("(()(()()))")
        10
        >>> s.longestValidParentheses("(())(())((()))()")
        16
        >>> s.longestValidParentheses("()()()")
        6
        >>> s.longestValidParentheses("()())()")
        4
        >>> s.longestValidParentheses("))(())(())((())))()((())()(()))())(((())))((())((((()()))()()((()())(()))))((((()()((())())())()))()))))(()))))()((())))())((()()))))(()))((((()(()))))(((((()(")
        68
        """
        s = s.lstrip(')').rstrip('(')

        length = len(s)
        if length < 2:
            return 0

        result = [[0 for col in range(length)] for row in range(length)]

        l = 1
        for i in range(0, length - l):
            j = i + l
            if s[i] == '(' and s[j] == ')':
                result[i][j] = 2
            else:
                result[i][j] = 0

        for l in range(2, length):
            for i in range(0, length - l):
                j = i + l

                if self.all_match(result, s, i, j):
                    result[i][j] = j - i + 1
                else:
                    result[i][j] = max(result[i+1][j], result[i][j-1])

        return result[0][length-1]






