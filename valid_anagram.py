__author__ = 'guang'

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        >>> s = Solution()
        >>> s.isAnagram("anagram", "nagaram")
        True
        >>> s.isAnagram("rat", "car")
        False
        """
        if len(s) != len(t):
        ascii = [chr(i + ord('a')) for i in range(26)]




