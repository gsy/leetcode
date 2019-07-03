# -*- coding: utf-8 -*-

from powerful_integers import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.powerfulIntegers(2, 3, 10)
    print(r)
    assert r == [2,3,4,5,7,9,10]


    r = s.powerfulIntegers(3, 5, 15)
    print(r)
    assert r == [2,4,6,8,10,14]

    r = s.powerfulIntegers(2, 1, 10)
    print(r)
    # assert r == [2, 3, 5, 9]

    r = s.powerfulIntegers(1, 1, 2)
    print(r)
    assert r == [2]
