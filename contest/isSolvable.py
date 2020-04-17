class Solution:
    def isSolvable(self, words, result):
        chars = set()
        mapping = {}

        for word in words:
            for char in word:
                chars.add(char)

        for char in chars:
            for c in range(10):
                # 所有的字符都完成之后，才能计算值
                ok = self.tryMapping(char, c, mapping)
                if ok:
