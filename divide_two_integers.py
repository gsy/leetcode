# -*- coding: utf-8 -*-


class Solution(object):
    def to_result(self, sign, result):
        if (sign == '+' and result > 2147483647) or (sign == '-' and result >= 2147483647):
            return 2147483647

        if sign == '+':
            return result
        else:
            return -result

    def divide(self, dividend, divisor):
        if divisor == 0:
            return None
        elif dividend == 0:
            return 0
        elif divisor == 1:
            return dividend

        sign = '+'
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = '-'

        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            return self.to_result(sign, dividend)

        count = 1
        a = divisor
        while a <= dividend:
            a = a + a
            count = count + count

        # a > dividend
        if a == dividend:
            return self.to_result(sign, count)
        else:
            print(a, dividend)
            while a > dividend:
                a = a - divisor
                count = count - 1

            return self.to_result(sign, count)


if __name__ == '__main__':
    s = Solution()
    r = s.divide(7, 3)
    print(r)
    assert r == 2

    r = s.divide(7, -3)
    assert r == -2

    r = s.divide(7, 0)
    assert r is None

    r = s.divide(0, 7)
    assert r == 0

    r = s.divide(0, 999999)
    assert r == 0

    r = s.divide(999999, 0)
    assert r is None

    r = s.divide(999999999, 1)
    assert r == 999999999

    r = s.divide(10, 3)
    assert r == 3

    r = s.divide(-2147483648, -1)
    assert r == 2147483647

    r = s.divide(2147483647, 2)
    assert r == 1073741823

    r = s.divide(-2147483648, 2)
    assert r == 1073741824
