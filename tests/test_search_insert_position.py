# -*- coding: utf-8 -*-

from search_insert_position import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.searchInsert([], 10)
    print(r)

    s = Solution()
    r = s.searchInsert([1, 3, 5, 6], 5)
    print(r)
    assert r == 2

    s = Solution()
    r = s.searchInsert([1, 3, 5, 6], 2)
    print(r)
    assert r == 1

    s = Solution()
    r = s.searchInsert([1, 3, 5, 6], 7)
    print(r)
    assert r == 4

    s = Solution()
    r = s.searchInsert([1, 3, 5, 6], 0)
    print(r)
    assert r == 0

    s = Solution()
    r = s.searchInsert([1, 3], 2)
    print(r)
    assert r == 1

    s = Solution()
    r = s.searchInsert([1, 3, 4, 10], 2)
    print(r)
    assert r == 1

    s = Solution()
    r = s.searchInsert([3, 5, 7, 9, 10], 8)
    print(r)
    assert r == 3
