# -*- coding: utf-8 -*-

from add_to_array import Solution

if __name__ == '__main__':
    s = Solution()
    r = s.addToArrayForm([1, 2, 0, 0], 35)
    print(r)
    assert r == [1, 2, 3, 5]

    r = s.addToArrayForm([1, 2, 0, 0], 0)
    print(r)
    assert r == [1, 2, 0, 0]

    r = s.addToArrayForm([], 3)
    print(r)
    assert r == [3]

    r = s.addToArrayForm([1,9,1,8], 99)
    print(r)
    assert r == [2, 0, 1, 7]
