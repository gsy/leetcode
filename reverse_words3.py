# -*- coding: utf-8 -*-


class Solution:
    def reverseWords(self, s):
        ls = []
        for word in s.split(' '):
            ls.append(word[::-1])
        return ' '.join(ls)


if __name__ == '__main__':
    s = Solution()
    r = s.reverseWords("Let's take LeetCode contest")
    assert r == "s'teL ekat edoCteeL tsetnoc"
