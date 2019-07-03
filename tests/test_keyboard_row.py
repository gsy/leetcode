# -*- coding: utf-8 -*-

from keyboard_row import Solution


if __name__ == '__main__':
    s = Solution()
    r = s.findWords([])
    print(r)
    assert r == []

    r = s.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(r)
    assert r == ['Alaska', 'Dad']
