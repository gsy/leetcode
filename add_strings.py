# -*- coding: utf-8 -*-


class Solution:
    def reverse(self, a):
        return a[::-1]

    def addStrings(self, num1, num2):
        a = self.reverse(num1)
        b = self.reverse(num2)
        len1 = len(a)
        len2 = len(b)
        common = min(len1, len2)

        carry = 0
        result = ""
        for i in range(common):
            _sum = int(a[i]) + int(b[i]) + carry
            if _sum >= 10:
                carry = int(_sum / 10)
                _sum = _sum % 10
            else:
                carry = 0
            result = result + str(_sum)

        for i in range(common, len1):
            _sum = int(a[i]) + carry
            if _sum >= 10:
                carry = int(_sum / 10)
                _sum = _sum % 10
            else:
                carry = 0
            result = result + str(_sum)

        for i in range(common, len2):
            _sum = int(b[i]) + carry
            if _sum >= 10:
                carry = int(_sum / 10)
                _sum = _sum % 10
            else:
                carry = 0
            result = result + str(_sum)

        if carry:
            result = result + str(carry)
        return self.reverse(result)
