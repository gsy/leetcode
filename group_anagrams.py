__author__ = 'guang'
import collections

class Solution(object):
    def hash_code(self, strs):
        """
        >>> s = Solution()
        >>> code1 = s.hash_code("tea")
        >>> code2 = s.hash_code("eat")
        >>> code3 = s.hash_code("tae")
        >>> code1 == code2 == code3
        True
        >>> code4 = s.hash_code("tdb")
        >>> code1 != code4
        True
        """
        code = 1
        for c in strs:
            code *= hash(c)

        return code

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        >>> s = Solution()
        >>> s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
        """
        if len(strs) == 0:
            return []

        table = collections.OrderedDict()

        for text in strs:
            key = self.hash_code(text)
            table[key] = table.get(key, []) + [text]

        for value in table.values():
            value.sort()

        return table.values()




