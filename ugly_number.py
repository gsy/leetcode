# -*- coding: utf-8 -*-

class Solution:
    def isUgly(self, num):
        if num < 1:
            return False
        dividents = [2, 3, 5]
        while num > 1:
            flag = False
            for divident in dividents:
                if num % divident == 0:
                    num = int(num / divident)
                    flag = True
                    break
            if flag is False:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    r = s.isUgly(6)
    assert r is True

    r = s.isUgly(8)
    assert r is True

    r = s.isUgly(14)
    assert r is False

    r = s.isUgly(15)
    assert r is True

    r = s.isUgly(1)
    assert r is True

    r = s.isUgly(-2147483648)
    assert r is False
