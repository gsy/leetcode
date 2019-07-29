# -*- coding: utf-8 -*-


class Solution:
    def word_count(self, word):
        result = {}
        for char in word:
            result[char] = result.get(char, 0) + 1
        return result

    def longestPalindrome(self, s):
        length = len(s)
        if length == 0:
            return 0

        count = self.word_count(s)
        # 如果有偶数个，那么可以放在中心点两边构成回文
        # 如果只有奇数个，那么多出来那个只能放在中心点，所以找出那个最长的奇数点
        # 剩下的可以取成最接近的偶数个
        print(count)
        even, odd, flag = 0, 0, 0
        for key, value in count.items():
            if value % 2 == 0:
                even = even + value
            else:
                flag = 1
                odd = odd + int(value / 2) * 2

        if flag:
            return even + odd + 1
        else:
            return even


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindrome("abccccdd")
    assert r == 7

    r = s.longestPalindrome("aA")
    assert r == 1

    r = s.longestPalindrome("aAa")
    assert r == 3

    r = s.longestPalindrome("a")
    assert r == 1

    r = s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
    assert r == 983
