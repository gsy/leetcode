# -*- coding: utf-8 -*-

class Solution:
    def numJewelsInStones(self, jewels, stones):
        return len([stone for stone in stones if stone in jewels])

if __name__ == "__main__":
    s = Solution()
    r = s.numJewelsInStones("aA", "aAAbbbb")
    print(r)
    assert r == 3
