class Solution:
    def sumZero(self, n):
        if n == 1:
            return [0]

        if n % 2 == 0:
            half = int(n / 2)
            return [i for i in range(1, half+1)] + [-i for i in range(1, half+1)]
        else:
            half = int((n + 1) / 2)
            return [i for i in range(half)] + [-i for i in range(1, half)]
