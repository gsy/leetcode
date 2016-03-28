__author__ = 'guang'

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        >>> s = Solution()
        >>> prices = [10, 3, 7, 8, 9, 15]
        >>> s.maxProfit(prices)
        12
        >>> prices = [1, 30, 3, 7, 8, 9, 15]
        >>> s.maxProfit(prices)
        29
        """
        if len(prices) <= 1:
            return 0

        result = -1
        minimum = prices[0]
        for index, price in enumerate(prices):
            if price < minimum:
                minimum = price

            profit = price - minimum
            if profit > result:
                result = profit

        return result








