__author__ = 'guang'

class Solution(object):
    def candidates(self, p):
        """

        :param p:
        :return:
        >>> s = Solution()
        >>> p = "aa"
        >>> s.candidates(p)
        ['aa']
        >>> s.candidates('.')
        ['.']
        >>> s.candidates('.a')
        ['.a']
        >>> s.candidates('a*b')
        ['aa*b', 'b']
        >>> s.candidates('c*a*b*')
        ['cc*a*b*', 'aa*b*', 'bb*']
        >>> s.candidates('.*')
        ['..*']
        >>> s.candidates('d*')
        ['dd*']
        >>> s.candidates('.*c')
        ['..*c', 'c']
        """
        if len(p) > 1 and p[1] == '*':
            extended = [p[0]]
            extended.extend(p)
            first = ''.join(extended)
            if len(p) <= 2:
                return [first]
            else:
                result = [first]
                result.extend(self.candidates(p[2:]))
                return result
        else:
            return [p]

    def reduce(self, p):
        """

        :param p:
        :return:
        >>> s = Solution()
        >>> s.reduce("a*b*")
        []
        >>> s.reduce("a*b*c")
        ['c']
        >>> s.reduce("a*bb*c")
        ['b', 'c']
        >>> s.reduce(".*c")
        ['c']
        """
        if len(p) == 0:
            return []

        result = []
        for i in range(len(p)-1):
            if p[i+1] != '*' and p[i] != '*':
                result.append(p[i])
        if p[len(p) - 1 ] != '*':
            result.append(p[len(p) - 1])

        return result

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        >>> s = Solution()
        >>> s.isMatch("aa", "a")
        False
        >>> s.isMatch("aa", "aa")
        True
        >>> s.isMatch("aaa", "aa")
        False
        >>> s.isMatch("aa", "a*")
        True
        >>> s.isMatch("abc", ".*")
        True
        >>> s.isMatch("aab", "c*a*b")
        True
        >>> s.isMatch("abcd", 'd*')
        False
        >>> s.isMatch("ab", ".*c")
        False
        >>> s.isMatch("aaa", "a*a")
        True
        """
        if len(s) == 0:
            if len(self.reduce(p)) == 0:
                return True
            else:
                return False

        if len(p) == 0:
            return False

        result = False
        for candidate in self.candidates(p):
            if s[0] == candidate[0] or candidate[0] == '.':
                if self.isMatch(s[1:], candidate[1:]):
                    return True

        return result
