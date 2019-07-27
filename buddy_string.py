# -*- coding: utf-8 -*-


class Solution:
    def buddyStrings(self, a, b):
        length1, length2 = len(a), len(b)
        if length1 != length2:
            return False
        elif length1 < 2:
            return False

        count = {}
        i, j = 0, length1 - 1
        while i < j:
            while a[i] == b[i] and i < j:
                count[a[i]] = count.get(a[i], 0) + 1
                i = i + 1
            while a[j] == b[j] and i < j:
                count[a[i]] = count.get(a[i], 0) + 1
                j = j - 1
            break

        if i == j:
            count[a[i]] = count.get(a[i], 0) + 1
            return any(item for item in count.values() if item >= 2)

        return a[i] == b[j] and a[j] == b[i] and a[i+1:j] == b[i+1:j]


if __name__ == '__main__':
    s = Solution()
    r = s.buddyStrings("ab", "ba")
    assert r is True

    # r = s.buddyStrings("ab", "ab")
    # assert r is False

    # r = s.buddyStrings("aaaaaaabc", "aaaaaaacb")
    # assert r is True

    r = s.buddyStrings("", "ab")
    assert r is False

    r = s.buddyStrings("aa", "aa")
    assert r is True

    r = s.buddyStrings("aabcd", "aabcd")
    assert r is True

    r = s.buddyStrings("abcd", "abcd")
    assert r is False

    r = s.buddyStrings("abab", "abab")
    assert r is True
