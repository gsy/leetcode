# -*- coding: utf-8 -*-

from hexadecimal import Solution

if __name__ == '__main__':
    s = Solution()
    r = s.toHex(26)
    print(r)
    assert r == "1a"

    r = s.toHex(100)
    print(r)
    assert r == "64"

    r = s.toHex(-1)
    print(r)
    assert r == "ffffffff"
