# -*- coding: utf-8 -*-


class Solution:
    def reverse(self, a):
        return a[::-1]

    def num_to_array(self, k):
        result = []
        while k > 0:
            digit = k % 10
            k = int(k / 10)
            result.append(digit)
        return result

    def addToArrayForm(self, a, k):
        a = self.reverse(a)
        b = self.num_to_array(k)
        len1 = len(a)
        len2 = len(b)
        common = min(len1, len2)

        carry = 0
        result = []
        for i in range(common):
            _sum = a[i] + b[i] + carry
            if _sum >= 10:
                carry = int(_sum / 10)
                _sum = _sum % 10
            else:
                carry = 0
            result.append(_sum)

        for i in range(common, len1):
            _sum = a[i] + carry
            if _sum >= 10:
                carry = int(_sum / 10)
                _sum = _sum % 10
            else:
                carry = 0
            result.append(_sum)

        for i in range(common, len2):
            _sum = b[i] + carry
            if _sum >= 10:
                carry = int(_sum / 10)
                _sum = _sum % 10
            else:
                carry = 0
            result.append(_sum)

        if carry:
            result.append(carry)
        return self.reverse(result)
