__author__ = 'guang'

class Solution(object):
    def candidates(self, p):
        """

        :param p:
        :return:
        >>> s = Solution()
        >>> s.candidates("aa")
        ['aa']
        >>> s.candidates("?*a")
        ['?*a']
        >>> s.candidates("*a")
        ['a', '?*a']
        >>> s.candidates("*")
        ['', '?*']
        """
        if p[0] == '*':
            return [p[1:], "?*" + p[1:]]
        else:
            return [p]

    def reduce(self, p):
        """

        :param p:
        :return:
        >>> s = Solution()
        >>> s.reduce("aa")
        'aa'
        >>> s.reduce('')
        ''
        """
        return ''.join([x for x in p if x != '*'])

    def patterns(self, p):
        result = []
        for pattern in p.split("*"):
            if pattern != '' and '?' not in pattern:
                result.append(pattern)

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
        >>> s.isMatch("aaa", "*")
        True
        >>> s.isMatch("aa", "a*")
        True
        >>> s.isMatch("ab", "?*")
        True
        >>> s.isMatch("aab", "c*a*b")
        False
        >>> s.isMatch("ba", "?*a")
        True
        >>> s.isMatch("bca", "??*a")
        True
        >>> s.isMatch("abcc","a*??")
        True
        >>> s.isMatch("aaab", "a*")
        True
        >>> s.isMatch("baabbabababaabbabababbaabbbbaaabaaabbbbaaaaaabbbbaaabaaabbbbbabaabbbbbbbbabbbabbabbbbabbbbabbbbbbabababbaaaabbbbaabaaababbbabaaaabaabbbabbaabbabbbbabaababbbbbbbabbaaaabaaabbaaabaaaaababbbaaaabbbbbabbabb", "ba*ba*bb*a********abaa*bb**abb**b***ab**b*b*babb***a*bb*aaabb*****b*aabb**aa**b*a***b*bb*b*bb*a*bbbbb**")
        False
        """
        if len(s) == 0:
            if self.reduce(p) == '':
                return True
            else:
                return False

        if len(p) == 0:
            return False

        for candidate in self.candidates(p):
            if candidate and (s[0] == candidate[0] or candidate[0] == '?') and self.isMatch(s[1:], candidate[1:]):
                    return True

        return False


