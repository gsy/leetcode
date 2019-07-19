# -*- coding: utf-8 -*-


class Solution:
    def is_self_dividing_number(self, num):
        if num == 0:
            return False

        tmp = num
        while tmp > 0:
            digit = tmp % 10
            tmp = int(tmp / 10)
            if digit == 0 or num % digit != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int):
        result = []
        for num in range(left, right + 1):
            if self.is_self_dividing_number(num):
                result.append(num)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.selfDividingNumbers(1, 22)
    assert r == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
