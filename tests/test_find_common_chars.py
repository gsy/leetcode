# -*- coding: utf-8 -*-

from find_common_chars import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.commonChars([])
    print(r)
    assert r == []

    r = s.commonChars(["bella", "label", "roller"])
    print(r)
    assert r == ["l", "l", 'e']

    r = s.commonChars(["cool", "lock", "cook"])
    print(r)
    assert r == ["c", "o"]

    r = s.commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"])
    print(r)
    assert r == []
