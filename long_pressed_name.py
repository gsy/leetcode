# -*- coding: utf-8 -*-

class Solution:
    def isLongPressedName(self, name, typed):
        length1, length2 = len(name), len(typed)
        if length1 > length2:
            return False

        prev,index  = None, 0
        for char in typed:
            if char == name[index]:
                index = index + 1
                prev = char
            elif prev != char:
                return False
            if index >= length1:
                break

        return index == length1

if __name__ == "__main__":
    s = Solution()
    r = s.isLongPressedName("alex", "aaleex")
    print(r)
    assert r is True

    r = s.isLongPressedName("saaeed", "ssaaedd")
    print(r)
    assert r is False

    r = s.isLongPressedName("leelee", "lleeelee")
    print(r)
    assert r is True

    r = s.isLongPressedName("guang", "guang")
    print(r)
    assert r is True

    r = s.isLongPressedName("vtkgn", "vttkgnn")
    print(r)
    assert r is True

    r = s.isLongPressedName("pyplrz", "ppyypllr")
    assert r is False
