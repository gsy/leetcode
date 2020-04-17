# -*- coding: utf-8 -*-


class Solution:
    def next_number(self, n):
        result = 0
        while n != 0:
            digit = (n % 10)
            result = result + (digit * digit)
            n = int(n/10)
        return result

    def isHappy(self, n):
        seen = set()
        while True:
            n = self.next_number(n)
            if n in seen:
                return False
            if n == 1:
                return True
            else:
                seen.add(n)


if __name__ == '__main__':
    s = Solution()
    r = s.isHappy(19)
    assert r is True

    r = s.isHappy(2)
    assert r is False
