# -*- coding: utf-8 -*-


class Solution:
    def convert(self, sign, number):
        if len(number) == 0:
            return 0

        if sign == '+':
            result = int(number)
            if result >= 2 ** 31:
                result = 2 ** 31 - 1
        else:
            result = int(number)
            if result > 2 ** 31:
                result = 2 ** 31
            result = -result
        return result

    def myAtoi(self, string):
        length = len(string)
        if length == 0:
            return 0

        self.state = "init"
        self.sign = None
        self.number = ""
        for char in string:
            if self.state == "init":
                if char == ' ':
                    continue
                elif char in ('+', '-'):
                    self.sign = char
                    self.state = "number"
                    continue
                elif char.isdigit():
                    self.sign = '+'
                    self.state = "number"
                else:
                    self.state = "invlid"
                    return 0

            if self.state == "number":
                if char.isdigit():
                    self.number = self.number + char
                else:
                    self.state = "done"
                    break

        return self.convert(self.sign, self.number)


if __name__ == '__main__':
    s = Solution()
    r = s.myAtoi("")
    assert r == 0

    r = s.myAtoi("1")
    assert r == 1

    r = s.myAtoi("123")
    assert r == 123

    r = s.myAtoi("-123")
    assert r == -123

    r = s.myAtoi("  -128")
    assert r == -128

    r = s.myAtoi("  4193 with words")
    assert r == 4193

    r = s.myAtoi("4193 with words")
    assert r == 4193

    r = s.myAtoi("words and 987")
    assert r == 0

    r = s.myAtoi("-91283472332")
    assert r == -2147483648

    r = s.myAtoi("+")
    assert r == 0
