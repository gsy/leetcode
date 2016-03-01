__author__ = 'guang'

class Solution(object):
    def binary_to_int(self, a):
        """
        >>> s = Solution()
        >>> s.binary_to_int("1")
        1
        >>> s.binary_to_int("111")
        7
        >>> s.binary_to_int("0")
        0
        >>> s.binary_to_int("100")
        4
        >>> s.binary_to_int("110010")
        50
        >>> s.binary_to_int("110")
        6
        """
        binary = int(a)
        result = 0
        base = 1
        while binary:
            result += base * (binary % 10)
            base *= 2
            binary /= 10

        return result

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        >>> s = Solution()
        >>> a = "11"
        >>> b = "1"
        >>> s.addBinary(a, b)
        '100'
        >>> a, b = "110", '111'
        >>> s.addBinary(a, b)
        '1101'
        >>> a, b = "110", '0'
        >>> s.addBinary(a, b)
        '110'
        >>> a, b = "110", '0'
        >>> s.addBinary(a, b)
        '110'
        >>> a, b = "100", "110010"
        >>> s.addBinary(a, b)
        '110110'
        """
        result = self.binary_to_int(a) + self.binary_to_int(b)
        result = bin(result)[2:]
        return result

