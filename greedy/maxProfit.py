class Solution:
    def maxProfit(self, prices):
        pre = None
        result = 0
        for price in prices:
            if pre is None:
                pre = price
                continue
            else:
                result = result + max(0, price - pre)
                pre = price

        return result
