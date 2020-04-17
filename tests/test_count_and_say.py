# -*- coding: utf-8 -*-

from count_and_say2 import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.countAndSay(1)
    print(r)
    assert r == "1"

    r = s.countAndSay(4)
    print(r)
    assert r == "1211"
