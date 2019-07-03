# -*- coding: utf-8 -*-


class Solution:
    def to_hex(self, num):
        if (num < 10):
            return str(num)
        else:
            return {
                10: "a",
                11: "b",
                12: "c",
                13: "d",
                14: "e",
                15: "f"
            }[num]

    def sign_to_hex(self, num):
        return {
            ""
        }

    def positive_to_hex(self, num):
        result = ""
        while num > 0:
            digit = self.to_hex(num % 16)
            num = int(num / 16)
            print(f"num {num}, digit {digit}")
            result = result + str(digit)
        return result[::-1]

    def toHex(self, num):
        if num > 0:
            return self.positive_to_hex(num)
        else:
            b = 2147483647 - 1 - num
            positive = self.positive_to_hex(b)
            sign = self.to_hex(16 - positive[0])
            positive[0] = sign
            return positive
