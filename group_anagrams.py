<<<<<<< HEAD
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




=======
# -*- coding: utf-8 -*-


class Solution:
    def hashing(self, string):
        count = {}
        for char in string:
            count[char] = count.get(char, 0) + 1
        result = ''
        for index in range(ord('a'), ord('z')+1):
            key = chr(index)
            if key in count:
                result = result + key + str(count[key])
        return result

    def groupAnagrams(self, strs):
        slots = {}
        for string in strs:
            key = self.hashing(string)
            slots[key] = slots.get(key, []) + [string]

        return list(slots.values())


if __name__ == '__main__':
    s = Solution()
    r = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(r)
>>>>>>> af85e649bb30ac65699bc91d8c414c7905d2f668
