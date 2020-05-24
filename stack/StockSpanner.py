#!/usr/bin/env python3

class StockSpanner:

    def __init__(self):
        self.prices = []
        self.length = 0


    def next(self, price: int) -> int:
        self.prices.append(price)
        self.length = self.length + 1

        count = 1
        for j in range(self.length-2, -1, -1):
            if self.prices[j] <= price:
                count = count + 1
            else:
                break

        return count




# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
r = obj.next(100)
print(r)
r = obj.next(80)
print(r)
r = obj.next(60)
print(r)
r = obj.next(70)
print(r)
r = obj.next(60)
print(r)
r = obj.next(75)
print(r)
r = obj.next(85)
print(r)
