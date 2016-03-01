class Solution(object):
    def next(self, number):
        """
        >>> s = Solution()
        >>> s.next("1")
        '11'
        >>> s.next("11")
        '21'
        >>> s.next("21")
        '1211'
        >>> s.next('1211')
        '111221'
        >>> s.next('111221')
        '312211'
        """
        result = ""

        i = 0
        while i < len(number):
            count = 0
            last = number[i]

            while i < len(number) and number[i] == last:
                i += 1
                count += 1
            result += str(count) + last

        return result

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        >>> s = Solution()
        >>> s.countAndSay(1)
        '1'
        >>> s.countAndSay(2)
        '11'
        >>> s.countAndSay(3)
        '21'
        """
        number = "1"

        for i in range(n - 1):
            number = self.next(number)

        return number

