# -*- coding: utf-8 -*-

from add_digits import Solution

if __name__ == '__main__':
    s = Solution()
    result = s.addDigits(38)
    print(result)
    assert result == 2

    result = s.addDigits(123)
    print(result)
    assert result == 6

    result = s.addDigits(10)
    print(result)
    assert result == 1
