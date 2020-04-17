# -*- coding: utf-8 -*-

from character_bits import Solution

if __name__ == '__main__':
    s = Solution()
    result = s.isOneBitCharacter([1, 0, 0])
    assert result is True

    result = s.isOneBitCharacter([1, 1, 1, 0])
    assert result is False

    result = s.isOneBitCharacter([1, 1, 0, 0])
    assert result is True

    result = s.isOneBitCharacter([1, 0, 1, 1, 0])
    assert result is True
