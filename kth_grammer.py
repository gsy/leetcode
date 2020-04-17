# -*- coding: utf-8 -*-


class Solution:
    def kthGrammar(self, lines, k):
        if lines == 1:
            return 0
        elif lines == 2:
            return 0 if k == 1 else 1
        else:
            index = int((k + 1) / 2)
            last_line = self.kthGrammar(lines-1, index)  # 上一行的变化出来的
            if last_line == 0:
                return 0 if k % 2 == 1 else 1
            else:
                return 1 if k % 2 == 1 else 0


if __name__ == '__main__':
    s = Solution()
    r = s.kthGrammar(3, 1)
    print(r)
    assert r == 0

    r = s.kthGrammar(3, 2)
    print(r)
    assert r == 1

    r = s.kthGrammar(3, 3)
    print(r)
    assert r == 1

    r = s.kthGrammar(3, 4)
    print(r)
    assert r == 0

    r = s.kthGrammar(4, 1)
    print(r)
    assert r == 0

    r = s.kthGrammar(4, 2)
    print(r)
    assert r == 1

    r = s.kthGrammar(4, 3)
    print(r)
    assert r == 1

    r = s.kthGrammar(4, 4)
    print(r)
    assert r == 0

    r = s.kthGrammar(4, 5)
    print(r)
    assert r == 1

    r = s.kthGrammar(4, 6)
    print(r)
    assert r == 0
