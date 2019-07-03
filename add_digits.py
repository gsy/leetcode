# -*- coding: utf-8 -*-


class Solution:
    def sum_of_digits(self, num):
        result = 0
        while num > 0:
            digit = num % 10
            num = int(num / 10)
            result += digit
        return result

    def addDigits(self, num):
        result = num
        while result >= 10:
            result = self.sum_of_digits(result)
        return result
