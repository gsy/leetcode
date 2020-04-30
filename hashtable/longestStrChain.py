class Word:
    def __init__(self, word):
        self.word = word
        self.length = len(word)
        self.depth = 1

    def __str__(self):
        return "{}:({})({})".format(self.word, self.length, self.depth)

    def __repr__(self):
        return "{}:({})({})".format(self.word, self.length, self.depth)


class Solution:
    def reachable(self, word1, word2):
        # word1 比 word2 多一个单词，只能多一个单词
        count1, count2 = {}, {}

        for char in word1:
            count1[char] = count1.get(char, 0) + 1
        for char in word2:
            count2[char] = count2.get(char, 0) + 1

        diff = 0
        for key in count1.keys():
            if key not in count2.keys():
                diff += 1
            elif count1[key] - count2[key] != 0:
                diff + 1

            if diff > 1:
                return False

        for key in count2.keys():
            if key not in count1.keys():
                diff += 1

            if diff > 1:
                return False

        return True

    def longestStrChain(self, words):
        if len(words) == 0:
            return 0

        ls = [Word(word) for word in words]
        ls = sorted(ls, key=lambda item: item.length)

        result = 1

        for i, word in enumerate(ls):
            for j in range(i-1, -1, -1):
                item = ls[j]
                if item.length == ls[i].length - 1:
                    if self.reachable(word.word, item.word) and (item.depth + 1) > word.depth:
                        word.depth = item.depth + 1
                        if word.depth >= result:
                            result = word.depth
                elif item.length < ls[i].length - 1:
                    break

        # print(ls)
        return result
