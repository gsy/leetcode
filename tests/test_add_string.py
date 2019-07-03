# -*- coding: utf-8 -*-

from add_strings import Solution

if __name__ == '__main__':
    s = Solution()
    r = s.addStrings("1", "2")
    print(r)
    assert r == "3"

    r = s.addStrings("8810", "1090")
    print(r)
    assert r == "9900"

    r = s.addStrings("1", "9")
    print(r)
    assert r == "10"
