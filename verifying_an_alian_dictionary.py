class Solution:
    def build_mapping(self, order):
        return {char: i for i, char in enumerate(order)}

    def compare(self, prev, current):
        length = len(current)
        for i, char in enumerate(prev):
            if i >= length:
                return 1

            a = self.mapping[char]
            b = self.mapping[current[i]]
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0

    def isAlienSorted(self, words, order):
        self.mapping = self.build_mapping(order)
        for i in range(0, len(words) - 1):
            prev, current = words[i], words[i+1]
            if self.compare(prev, current) > 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    r = s.isAlienSorted(words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
    assert r is True

    r = s.isAlienSorted(words=["word","world","row"], order="worldabcefghijkmnpqstuvxyz")
    assert r is False

    r = s.isAlienSorted(words=["apple","app"], order="abcdefghijklmnopqrstuvwxyz")
    assert r is False
