class Solution(object):
    def match(self, s, start, length, dictionary, unit):
        """
        >>> s = Solution()
        >>> text = "barfoothefoobarman"
        >>> words = {"foo": 1, "bar": 1}
        >>> length = 6
        >>> s.match(text, 0, length, words, 3)
        True
        >>> s.match(text, 3, length, words, 3)
        False
        >>> s.match(text, 6, length, words, 3)
        False
        >>> s.match(text, 9, length, words, 3)
        True
        >>> s.match(text, 15, length, words, 3)
        False
        """
        copy = dictionary.copy()
        count = 0
        while count < length / unit:
            count += 1
            word = s[start:start+unit]
            if word in copy and copy[word] > 0:
                start += unit
                copy[word] -= 1
            else:
                return False

        return True

    def dictionary(self, words):
        """
        >>> s = Solution()
        >>> s.dictionary(["foo", "bar"])
        {'foo': 1, 'bar': 1}
        >>> s.dictionary(["foo", "foo", "bar", "the"])
        {'the': 1, 'foo': 2, 'bar': 1}
        """
        result = {}
        keys = set(words)

        for key in keys:
            result[key] = words.count(key)

        return result

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        >>> s = Solution()
        >>> s.findSubstring("barfoothefoobarman", ["foo", "bar"])
        [0, 9]
        >>> s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
        [6, 9, 12]
        >>> s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
        [13]
        """
        if len(words) == 0:
            return []

        word_unit = len(words[0])
        word_count = len(words)
        length = word_unit * word_count
        total = len(s)
        result = []
        d = self.dictionary(words)

        i = 0
        while i + length <= total:
            if self.match(s, i, length, d, word_unit):
                result.append(i)

            i += 1

        return result
