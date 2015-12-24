__author__ = 'guang'

class Solution(object):
    def combination(self, candidates1, a, candidates2, b):
        """
        >>> s = Solution()
        >>> s.combination(["()"], 1, ["()"], 1)
        ['(())', '()()']
        >>> s.combination(["()"], 1, ["(())", "()()"], 2)
        ['((()))', '()(())', '(())()', '(()())', '()()()']
        >>> s.combination(["(())", "()()"], 2, ["(())", "()()"], 2)
        ['(())(())', '(())()()', '()()(())', '()()()()']
        >>> s.combination(["()"], 1, ['((()))', '()(())', '(())()', '(()())', '()()()'], 3)
        ['(((())))', '()((()))', '((()))()', '(()(()))', '()()(())', '()(())()', '((())())', '()(())()', '(())()()', '((()()))', '()(()())', '(()())()', '(()()())', '()()()()']
        """
        result = []
        for x in candidates1:
            for y in candidates2:
                if x == "()":
                    result.append("(" + y + ")")
                result.append(x + y)
                if a != b and y + x not in result:
                    result.append(y + x)
        return result

    def generate(self, parenthese, n):
        """
        >>> s = Solution()
        >>> result = s.generate([[], ["()",]], 2)
        >>> result == set(['(())', '()()'])
        True
        >>> candidates = [[], ["()"], ["(())", "()()"]]
        >>> result = s.generate(candidates, 3)
        >>> result == set(['((()))', '()(())', '(())()', '(()())', '()()()'])
        True
        """
        result = set()

        for a in range(1, n/2+1):
            b = n - a
            candidates1 = parenthese[a]
            candidates2 = parenthese[b]
            combinations = self.combination(candidates1, a, candidates2, b)
            result.update(combinations)

        return result

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        >>> s = Solution()
        >>> result = set(s.generateParenthesis(3))
        >>> expected = set(['((()))', '()(())', '(())()', '(()())', '()()()'])
        >>> result == expected
        True
        >>> result = set(s.generateParenthesis(4))
        >>> expected = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
        >>> result == expected
        True
        """
        result = [[], ["()", ]]
        for i in range(2, n+1):
            parenthesis = self.generate(result, i)
            result.append(list(parenthesis))

        return result[n]








