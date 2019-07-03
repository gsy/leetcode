# -*- coding: utf-8 -*-

from binary_search import Solution


if __name__ == '__main__':
    s = Solution()
    # r = s.search([-1,0,3,5,9,12], 9)
    # print(r)
    # assert r == 4

    # r = s.search([], 9)
    # print(r)
    # assert r == -1

    # r = s.search([1, 2, 9], 9)
    # print(r)
    # assert r == 2

    # r = s.search([1, 2, 9], 1)
    # print(r)
    # assert r == 0

    r = s.search([-1,0,3,5,9,12], 13)
    print(r)
    assert r == -1
