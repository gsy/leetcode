# -*- coding: utf-8 -*-


class Solution:
    def getHint(self, secret, guess):
        # A, bulls: 数字和位置都对
        # B, cows: 数字是对的，但是位置不对

        length = len(guess)
        if length == 0:
            return ""

        bulls, cows, wrong, right = 0, 0, {}, {}
        for i in range(length):
            if secret[i] == guess[i]:
                bulls = bulls + 1
            right[secret[i]] = right.get(secret[i], 0) + 1
            wrong[guess[i]] = wrong.get(guess[i], 0) + 1

        return "{}A{}B".format(bulls, cows)


if __name__ == '__main__':
    s = Solution()
    r = s.getHint("1807", "7810")
    print(r)
    assert r == "1A3B"

    r = s.getHint("1123", "0111")
    assert r == "1A1B"
