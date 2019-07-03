# -*- coding: utf-8 -*-

from twokey_keyboard import Solution

if __name__ == '__main__':
    s = Solution()
    result = s.minSteps(9)
    print(result)
    assert result == 6

    result = s.minSteps(6)
    print(result)
    assert result == 5

    result = s.minSteps(12)
    print(result)
    assert result == 7
