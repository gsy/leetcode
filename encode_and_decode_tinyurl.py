# -*- coding: utf-8 -*-

import string

class Codec:
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + "-"
        self.base = len(self.alphabet)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # 可逆的编码方式，编码后字符串的长度变小
        # 换成高进制的数字？
        num = 0
        for char in longUrl:
            num = num + (ord(char) % self.base)
            num = num * self.base

        return str(num)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        num, result = int(shortUrl), ""
        while num > 0:
            current = num % self.base
            result = result + chr(current)
            num = num / self.base
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
if __name__ == "__main__":
    url = "https://leetcode/com/problems/design-tinyurl"
    codec = Codec()
    encoded = codec.encode(url)
    print(encoded)
    r = codec.decode(encoded)
    print(r)
    assert r == url
