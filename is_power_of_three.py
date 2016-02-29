import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        result = math.log10(n) / math.log10(3)
        return result % 1 == 0
