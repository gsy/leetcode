# -*- coding: utf-8 -*-


class Solution:
    def reverse(self, string):
        result = []
        for i in range(len(string) - 1, -1, -1):
            result.append(string[i])
        return ''.join(result)

    def addBinary(self, a, b):
        a = self.reverse(a)
        b = self.reverse(b)
        length1 = len(a)
        length2 = len(b)
        common = min(length1, length2)

        result = []
        carry = 0
        # print(f"a {a}, b {b}")
        for i in range(common):
            total = int(a[i]) + int(b[i]) + carry
            if total >= 2:
                carry = int(total / 2)
                total = total % 2
            else:
                carry = 0
            result.append(str(total))

        for i in range(common, length1):
            total = int(a[i]) + carry
            if total >= 2:
                carry = int(total / 2)
                total = total % 2
            else:
                carry = 0
            result.append(str(total))

        for i in range(common, length2):
            total = int(b[i]) + carry
            if total >= 2:
                carry = int(total / 2)
                total = total % 2
            else:
                carry = 0
            result.append(str(total))
        if carry:
            result.append(str(carry))

        return self.reverse(''.join(result))
