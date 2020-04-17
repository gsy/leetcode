class Solution:
    def wordCount(self, word):
        count = {}
        for char in word:
            count[char] = count.get(char, 0) + 1

        return count

    def master(self, word, chars):
        count = self.wordCount(word)
        for char in word:
            if (char not in chars) or (chars[char] < count[char]):
                return False

        return True

    def countCharacters(self, words, chars):
        result = 0
        count = self.wordCount(chars)

        for word in words:
            if self.master(word, count):
                result = result + len(word)

        return result
