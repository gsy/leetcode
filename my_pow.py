class Solution(object):
    def my_pow_helper(self, x, n, result):
        if n in result:
            return result[n]

        answer = self.my_pow_helper(x, n / 2, result) * self.my_pow_helper(x, n - n / 2, result)
        result[n] = answer
        return answer

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        >>> s = Solution()
        >>> s.myPow(3, 0)
        1
        >>> s.myPow(3, 1)
        3
        >>> s.myPow(3, 2)
        9
        >>> s.myPow(3, 3)
        27
        >>> s.myPow(3, 4)
        81
        >>> s.myPow(3, 5)
        243
        >>> s.myPow(3, -1)
        0.3333333333333333
        >>> s.myPow(-3, 0)
        1
        >>> s.myPow(-3, 1)
        -3
        >>> s.myPow(-3, 2)
        9
        >>> s.myPow(0.00001, 2147483647)
        0
        >>> s.myPow(1.00000, 2147483647)
        1
        >>> s.myPow(2.00000, -2147483648)
        0.0
        >>> s.myPow(2.00000, 2147483647)
        inf
        >>> s.myPow(0.99999, 948688)
        0.00008
        """

        if n < 0:
            return 1.0 / self.myPow(x, -n)

        if n - 0 <= 0.00001:
            return 1

        if abs(x - 0) <= 0.00001:
            return 0

        if x == 1:
            return 1

        i = 1
        base = x
        result = {}
        while i <= n:
            result[i] = base
            i *= 2
            base = base * base

        return self.my_pow_helper(x, n, result)
