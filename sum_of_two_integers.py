# -*- coding: utf-8 -*-

class Solution:
    def bit_plus(self, a, b, carry):
        return (a ^ b) ^ carry, (a & b) | (a ^ b) & carry

    def getSum(self, a, b):
        digit, carry, result = 1, 0, 0
        while True:
            a_bit = a & digit
            b_bit = b & digit
            if a_bit == 0 and b_bit == 0:
                break
            tmp, carry = self.bit_plus(a_bit, b_bit, carry)
            result = result | tmp
            digit = digit << 1
        print(result, carry)

        if carry:
            return digit ^ result
        else:
            return result

if __name__ == "__main__":
    s = Solution()
    r = s.getSum(1, 1)
    print(r)

    r = s.getSum(1, 2)
    print(r)

    r = s.getSum(1, 3)
    print(r)
