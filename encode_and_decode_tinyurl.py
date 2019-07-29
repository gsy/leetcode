# -*- coding: utf-8 -*-

class Codec:
    def __init__(self):
        self.count = 1
        self.mapping = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # 可逆的编码方式，编码后字符串的长度变小
        self.mapping[self.count] = longUrl
        url = "http://tinyurl.com/" + str(self.count)
        self.count = self.count + 1
        return url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        count = shortUrl.split("/")[-1]
        return self.mapping[int(count)]


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
