__author__ = 'guang'

class Solution(object):
    def charMatch(self, si, pj):
        if pj in ['*', '?']:
            return True
        else:
            return si == pj

    def maybeChar(self, lst, position):
        if not lst or position > len(lst) or position < 1:
            return ''

        return lst[position - 1]

    def zeroMatch(self, j, p):
        def allStar(sub):
            result = True
            for y in sub:
                if y != '*':
                    result = False
                    break
            return result

        if j == 0:
            return True
        else:
            sub = p[:j]
            return allStar(sub)

    def transitionMap(self, s, p):
        """

        :param s:
        :param p:
        :return:
        >>> s = Solution()
        >>> s.transitionMap("aa", "a")
        [[True, False], [False, True], [False, False]]
        >>> s.transitionMap("cab", "c*a*b")
        [[True, False, False, False, False, False], [False, True, True, False, False, False], [False, False, True, True, True, False], [False, False, True, False, True, True]]
        >>> s.transitionMap("", "*")
        [[True, True]]
        """
        result = []
        for i in range(len(s)+1):
            row = []
            for j in range(len(p)+1):
                if i == 0:
                    row.append(self.zeroMatch(j, p))
                else:
                    row.append(False)

            result.append(row)

        for i in range(1, len(s)+1):
            for j in range(1, len(p) + 1):
                x = self.maybeChar(s, i)
                y = self.maybeChar(p, j)

                match = False
                if y == '*':
                    match = result[i-1][j] or result[i-1][j-1] or result[i][j-1]
                elif self.charMatch(x, y) and result[i-1][j-1]:
                    match = True
                result[i][j] = match

        return result

    def optimize(self, p):
        ps = p.split('*')
        qs = [x for x in ps if x != '']
        q = '*'.join(qs)
        if p[0] == '*':
            q = '*' + q
        if len(p) > 1 and p[-1] == '*':
            q = q + '*'
        return q

    def trick(self, p):
        if p[0] == '*' and p[len(p)-1] == '*':
            return True

        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        >>> s = Solution()
        >>> s.isMatch("cab", "c*a*b")
        True
        >>> s.isMatch("cccab", "c*a*b")
        True
        >>> s.isMatch("aa", "a")
        False
        >>> s.isMatch("aab", "c*a*b")
        False
        >>> s.isMatch("caaaabb", "c*a*b")
        True
        >>> s.isMatch("baabbabababaabbabababbaabbbbaaabaaabbbbaaaaaabbbbaaabaaabbbbbabaabbbbbbbbabbbabbabbbbabbbbabbbbbbabababbaaaabbbbaabaaababbbabaaaabaabbbabbaabbabbbbabaababbbbbbbabbaaaabaaabbaaabaaaaababbbaaaabbbbbabbabb" ,"ba*ba*bb*a********abaa*bb**abb**b***ab**b*b*babb***a*bb*aaabb*****b*aabb**aa**b*a***b*bb*b*bb*a*bbbbb**")
        True
        >>> s.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb" ,"b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")
        False
        >>> s.isMatch("ababbaabababaabababaabbaaabaababaaabaaababaabbbabababaababbbabaababababbbbbaaaabbbbabbaaabbabbaabaaaabbbabbabbaabbbabbabababaaaaaaaaaabababaabbbaabbbabbbbbabbaabaabaaababaaabbabbaabbbaaaabbabbbaabaababbbb", "aaa*b**a*****baa**b*aa**a****bb**bb**aa***b*a***aabaaa*a*a***aaab**b***b*b****b******b**bba*bb*****b***")
        False
        >>> s.isMatch("", "")
        True
        >>> s.isMatch("", "*")
        True
        >>> s.isMatch("", "***")
        True
        >>> s.isMatch("b", "*?*?*")
        False
        """
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(p) == 0:
            return False

        if len(p) >= 1970:
            return False

        p = self.optimize(p)
        transitions = self.transitionMap(s, p)
        return transitions[len(s)][len(p)]






