# -*- coding: utf-8 -*-

from add_binary import Solution

if __name__ == '__main__':
    s = Solution()
    r = s.reverse("100")
    print(r)

    r = s.addBinary("100", "1")
    print(r)
    assert r == '101'

    r = s.addBinary("00", "00")
    print(r)
    assert r == '00'

    r = s.addBinary("00", "01")
    print(r)
    assert r == '01'

    r = s.addBinary("00", "10")
    print(r)
    assert r == '10'

    r = s.addBinary("10", "10")
    print(r)
    assert r == '100'

    r = s.addBinary("10", "11")
    print(r)
    assert r == '101'

    r = s.addBinary("11", "11")
    print(r)
    assert r == '110'

    r = s.addBinary("1010", "1011")
    print(r)
    assert r == '10101'
