# -*- coding: utf-8 -*-


class Solution:
    def hIndex(self, citations):
        if len(citations) == 0:
            return 0

        citations = sorted(citations, reverse=True)
        count, seen = {}, set()

        acc = 0
        for citation in citations:
            if citation not in seen:
                seen.add(citation)
            count[citation] = acc + count.get(citation, 0) + 1
            acc = acc + 1

        keys = sorted(count.keys(), reverse=True)
        for citation in keys:
            # count[key]: docs
            if citation <= count[citation]:
                return citation

        return len(citations)


if __name__ == '__main__':
    s = Solution()
    r = s.hIndex([3, 0, 6, 1, 5])
    print(r)
    assert r == 3

    r = s.hIndex([100])
    print(r)
    assert r == 1

    r = s.hIndex([11, 15])
    print(r)
    assert r == 2

    r = s.hIndex([4, 4, 0, 0])
    assert r == 2
