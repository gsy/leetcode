# -*- coding: utf-8 -*-


class Solution:
    def reverseOnlyLetters(self, string):
        length = len(string)
        if length == 0:
            return ""

        start, end, left, right = 0, length - 1, "", ""
        while start <= end:
            while start < length and (not string[start].isalpha()):
                if start > end:
                    break
                left = left + string[start]
                start = start + 1

            while end > 0 and (not string[end].isalpha()):
                if start >= end:
                    break
                right = string[end] + right
                end = end - 1

            if start > end:
                break

            if start < end:
                right = string[start] + right
            left = left + string[end]
            start = start + 1
            end = end - 1

        return left + right


if __name__ == "__main__":
    s = Solution()
    r = s.reverseOnlyLetters("")
    assert r == ""

    r = s.reverseOnlyLetters("ab-cd")
    print(r)
    assert r == "dc-ba"

    r = s.reverseOnlyLetters("a-bC-dEf-ghIj")
    print(r)
    assert r == "j-Ih-gfE-dCba"

    r = s.reverseOnlyLetters("Test1ng-Leet=code-Q!")
    print(r)
    assert r == "Qedo1ct-eeLg=ntse-T!"

    r = s.reverseOnlyLetters("-")
    assert r == "-"

    r = s.reverseOnlyLetters("----")
    assert r == "----"

    r = s.reverseOnlyLetters("---a")
    assert r == "---a"
