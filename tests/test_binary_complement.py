# -*- coding: utf-8 -*-

from binary_complement import Solution

if __name__ == '__main__':
    s = Solution()
    r = s.bitwiseComplement(5)
    print(r)
    assert r == 2

    r = s.bitwiseComplement(7)
    print(r)
    assert r == 0

    r = s.bitwiseComplement(10)
    print(r)
    assert r == 5

    r = s.bitwiseComplement(0)
    print(r)
    assert r == 1
