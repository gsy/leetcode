# -*- coding: utf-8 -*-


class Solution:
    def detectCapitalUse(self, word):
        state = ''
        for char in word:
            if char.isupper():
                if state == '':
                    state = 'initial'
                elif state == 'lower':
                    return False
                elif state == 'initial':
                    state = "upper"
            else:
                if state == '':
                    state = 'lower'
                if state == 'initial':
                    state = 'lower'
                elif state == 'upper':
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    r = s.detectCapitalUse("usa")
    assert r is True

    r = s.detectCapitalUse("Usa")
    assert r is True

    r = s.detectCapitalUse("USA")
    assert r is True

    r = s.detectCapitalUse("uSA")
    assert r is False

    r = s.detectCapitalUse("FlaG")
    assert r is False
