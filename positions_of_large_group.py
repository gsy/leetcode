# -*- coding: utf-8 -*-


class Solution:
    def largeGroupPositions(self, string):
        length = len(string)
        if length == 0:
            return []

        result = []
        prev, start, end, count = None, None, None, 1
        for index, current in enumerate(string + "#"):
            if prev is None:
                prev = current
                start = index
                continue

            if current == prev:
                count = count + 1
                end = index
            else:
                if count >= 3:
                    result.append([start, end])
                prev = current
                start = index
                count = 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.largeGroupPositions('abc')
    assert r == []

    r = s.largeGroupPositions('abbxxxxzzy')
    print(r)
    assert r == [[3, 6]]

    r = s.largeGroupPositions('abcdddeeeeaabbbcd')
    assert r == [[3, 5], [6, 9], [12, 14]]

    r = s.largeGroupPositions("aaa")
    print(r)
    assert r == [[0, 2]]

    r = s.largeGroupPositions("aaacbbbbb")
    print(r)
    assert r == [[0, 2], [4, 8]]
