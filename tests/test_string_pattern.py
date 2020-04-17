# -*- coding: utf-8 -*-

from string_pattern import Solution

if __name__ == '__main__':
    s = Solution()
    result = s.find132pattern([3, 1, 4, 2])
    assert result is True

    result = s.find132pattern([-1, 3, 2, 0])
    assert result is True

    result = s.find132pattern([1, 2, 3, 4])
    assert result is False

    result = s.find132pattern([5, 1, 4, 3, -4, 10])
    assert result is True

    result = s.find132pattern([1, 0, 1, -4, -3])
    assert result is False

    result = s.find132pattern([-2,1,2,-2,1,2])
    assert result is True
