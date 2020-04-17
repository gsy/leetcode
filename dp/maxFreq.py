class Solution:
    def valid(self, sub, maxLetters):
        chars = set([char for char in sub])
        return len(chars) <= maxLetters

    def maxFreq(self, s, maxLetters, minSize,  maxSize):
        length = len(s)
        count = {}

        for i in range(length):
            for j in range(minSize, maxSize+1):
                if i + j > length:
                    break

                sub = s[i: i+j]
                if self.valid(sub, maxLetters):
                    count[sub] = count.get(sub, 0) + 1

        result = 0
        for sub, value in count.items():
            if value > result:
                result = value

        return result
