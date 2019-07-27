# -*- coding: utf-8 -*-


class Solution:
    def isIsomorphic(self, s, t):
        mapping, seen = {}, set()
        for s_char, t_char in zip(s, t):
            if mapping.get(s_char, None) is None:
                if t_char in seen:
                    return False
                mapping[s_char] = t_char
                seen.add(t_char)
            elif mapping[s_char] != t_char:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isIsomorphic("egg", "add")
    assert r is True

    r = s.isIsomorphic("foo", "bar")
    assert r is False

    r = s.isIsomorphic("paper", "title")
    assert r is True

    r = s.isIsomorphic("foa", "bar")
    assert r is True

    r = s.isIsomorphic("aa", "ab")
    assert r is False

    r = s.isIsomorphic("ab", "aa")
    assert r is False
