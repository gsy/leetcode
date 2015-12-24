__author__ = 'guang'

class Solution(object):
    def __init__(self):
        self.digitLetterMapping = {'0': "", '1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

    def combine(self, digit, sub):
        """
        >>> s = Solution()
        >>> s.combine('3', [])
        ['d', 'e', 'f']
        >>> s.combine('2', ['d', 'e', 'f'])
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        """
        letters = self.digitLetterMapping[digit]
        if not sub:
            return list(letters)

        result = []
        for c in self.digitLetterMapping[digit]:
            for s in sub:
                result.append(c + s)

        return result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        >>> s = Solution()
        >>> s.letterCombinations("2")
        ['a', 'b', 'c']
        >>> s.letterCombinations("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        """
        if len(digits) == 0:
            return []

        result = []
        for digit in digits[::-1]:
            result = self.combine(digit, result)

        return result







