__author__ = 'guang'

class Solution(object):
    def valid(self, s):
        """
        >>> s = Solution()
        >>> text = "(()(()"
        >>> result = s.valid(text)
        >>> result
        [1, 2, 4, 5]
        >>> text = "((((()(()))))"
        >>> result = s.valid(text)
        >>> result.sort()
        >>> result
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        """
        stack = []
        result = set()

        for index, item in enumerate(s):
            if item == '(':
                stack.append(index)
            elif len(stack) > 0:
                result.add(stack.pop())
                result.add(index)

        return frozenset(result)

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
        >>> s.longestValidParentheses("()())")
        4
        >>> s.longestValidParentheses("((((()(()))))")
        12
        >>> s.longestValidParentheses("(()(()")
        2
        >>> s.longestValidParentheses("(()(())")
        6
        >>> s.longestValidParentheses("(()()(")
        4
        >>> s.longestValidParentheses("()())((((()(()))))()((()(()(())()))(()((()(())(((()((())())(((())(())())()()(()((((((()()(()())()))())()((()())((((((())()()()))(((()()((()()(()((((()))((()))(()(()())()(()((())())))(()()())()((((())")
        46
        """
        s = s.lstrip(')').rstrip('(')

        length = len(s)
        if length < 2:
            return 0

        last_value = 0
        result = 0
        valid = self.valid(s)

        for index, c in enumerate(s):
            if c == '(':
                if index not in valid:
                    last_value = 0
            else:
                if index in valid:
                    last_value += 2
                else:
                    last_value = 0

            if last_value > result:
                result = last_value

        return result
