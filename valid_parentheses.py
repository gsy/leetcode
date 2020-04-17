__author__ = 'guang'

class Solution(object):
    def match(self, x, y):
        return (x, y) in [('(', ')'), ('[', ']'), ('{', '}')]

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        >>> s = Solution()
        >>> s.isValid("{{}}")
        True
        >>> s.isValid("[{}])")
        False
        >>> s.isValid("(}")
        False
        >>> s.isValid("")
        True
        >>> s.isValid("([]")
        False
        """

        if len(s) == 0:
            return True

        open = ['(', '[', '{']
        close = [')', ']', '}']

        if s[-1] in open:
            return False

        stack = []
        for x in s:
            if x in open:
                stack.append(x)
            else:
                if not stack:
                    return False
                else:
                    y = stack.pop()
                    if not self.match(y, x):
                        return False

        return len(stack) == 0
