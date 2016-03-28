__author__ = 'guang'

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        >>> s = Solution()
        >>> s.wordPattern("abba", "dog cat cat dog")
        True
        >>> s.wordPattern("abba", "dog cat cat fish")
        False
        >>> s.wordPattern("aaaa", "dog cat cat dog")
        False
        >>> s.wordPattern("aaaa", "dog dog dog dog")
        True
        >>> s.wordPattern("abba", "dog dog dog dog")
        False
        """
        mapping = {}
        str_list = str.split()

        if len(str_list) != len(pattern):
            return False

        for p, s in zip(pattern, str.split()):
            if p in mapping:
                if mapping[p] != s:
                    return False
            else:
                if s in mapping.values():
                    return False

                mapping[p] = s

        return True
