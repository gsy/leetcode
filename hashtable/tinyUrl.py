class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        result = []
        for char in longUrl:
            result.append(str(ord(char)))

        return "http://tinyurl.com/" + "#".join(result)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        tmp = shortUrl.split('/')[-1]
        result = ""
        for char in tmp.split('#'):
            result = result + chr(int(char))

        return result


# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "www.zhihu.com"
encoded = codec.encode(url)
print("encoded", encoded)
decoded = codec.decode(encoded)
print("decoded", decoded)
