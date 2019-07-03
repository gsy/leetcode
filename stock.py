# -*- coding: utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        result = 0
        minimum = prices[0]
        for index, price in enumerate(prices):
            if price < minimum:
                minimum = price

            profit = price - minimum
            if profit > result:
                result = profit

        return result
