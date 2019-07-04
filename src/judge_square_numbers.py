# -*- coding: utf-8 -*-


class Solution:
    def generate_square_numbers(self, limit):
        num, result =0, []
        while True:
            target = num * num
            if target > limit:
                break
            else:
                result.append(target)
                num = num + 1
        return result

    def find_squares(self, squares, target):
        length = len(squares)
        if length == 0:
            return False

        left, right = 0, length - 1
        while left <= right:
            middle = int((left + right) / 2)
            value = squares[middle]
            if value == target:
                return True
            elif value > target:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def judgeSquareSum(self, c):
        if c <= 2:
            return True

        square_numbers = self.generate_square_numbers(c)
        for a in square_numbers:
            b = c - a
            if self.find_squares(square_numbers, b):
                return True
        return False



if __name__ == "__main__":
    s = Solution()
    r = s.judgeSquareSum(1)
    assert r is True

    r = s.judgeSquareSum(2)
    assert r is True

    r = s.judgeSquareSum(3)
    assert r is False

    r = s.judgeSquareSum(4)
    assert r is True

    r = s.judgeSquareSum(5)
    assert r is True

    r = s.judgeSquareSum(6)
    assert r is False

    r = s.judgeSquareSum(7)
    assert r is False

    r = s.judgeSquareSum(8)
    assert r is True

    r = s.judgeSquareSum(9)
    assert r is True

    r = s.judgeSquareSum(999999999)
    assert r is False

    r = s.judgeSquareSum(78379897)
    assert r is True

    r = s.judgeSquareSum(11111)
    assert r is False
