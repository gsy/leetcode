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
            return False

        ascii = [chr(i + ord('a')) for i in range(26)]
        table1 = {}
        table2 = {}

        for c in ascii:
            table1[c] = s.count(c)
            table2[c] = t.count(c)

        for key in ascii:
            if table1.get(key, 0) != table2.get(key, 0):
                return False

        return True
