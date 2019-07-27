# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.primes = {}
        self.limit = 1000
        for tester in range([2, 3, 5, 7, 9, 11]):
            current = tester
            while current < self.limit:
                self.primes[current] = 0
                current = current * 2

    def countPrimes(self, n):
        count = 0
        for x in range(2, n):
            if self.primes.get(x, 0):
                count = count + 1

        return count


if __name__ == '__main__':
    s = Solution()
    r = s.countPrimes(10)
    assert r == 4
