__author__ = 'guang'

class Solution(object):
    def transitions(self, p):
        """
        :param p:
        :return:
        >>> s = Solution()
        >>> s.transitions("aa")
        [{'a': 1}, {'a': 2}]
        >>> s.transitions("a")
        [{'a': 1}]
        >>> s.transitions("?a")
        [{'?': 1}, {'a': 2}]
        >>> s.transitions("*")
        [{'?': 0}]
        >>> s.transitions("a*")
        [{'a': 1}, {'?': 1}]
        >>> s.transitions("c*a*b")
        [{'c': 1}, {'a': 2, '?': 1}, {'b': 3, '?': 2}]
        """
        result = []
        state = 0
        length = len(p)
        for index, x in enumerate(p):
            mapping = {}
            state += 1
            if x == '*':
                mapping['?'] = state - 1
                if index < length - 1:
                    mapping[p[index+1]] = state
            else:
                if index > 0 and p[index - 1] == '*':
                    state -= 1
                    continue
                else:
                    mapping[x] = state
            result.append(mapping)

        return result

    def accepting_state(self, transitions):
        mapping = transitions[-1]
        return mapping.values()

    def judge(self, state, s, transitions):
        if len(s) == 0:
            return state in self.accepting_state(transitions)
        elif state >= len(transitions):
            return False

        mapping = transitions[state]
        possibles = mapping.keys()
        x = s[0]

        if x in possibles:
            next_state = mapping[x]
            if self.judge(next_state, s[1:], transitions):
                return True
        if '?' in possibles:
            next_state = mapping['?']
            if self.judge(next_state, s[1:], transitions):
                return True
            elif next_state != state:
                return self.judge(next_state, s, transitions)

        return False

    def optimize(self, p):
        if len(p) == 0:
            return []

        ps = p.split('*')
        qs = [x for x in ps if x != '']
        q = '*'.join(qs)
        result = q
        if p[0] == '*':
            result = "*" + result
        if len(p) > 1 and p[-1] == '*':
            result = result + "*"
        return result

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
        """
        if len(s) == 0:
            return False

        p = self.optimize(p)
        return self.judge(0, s, self.transitions(p))





