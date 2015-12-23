__author__ = 'guang'

import string

class Solution(object):
    def minPostion(self, pairs):
        """

        :param pairs:
        :return:
        >>> s = Solution()
        >>> s.minPostion([])
        0
        >>> s.minPostion([6, 3, 9])
        1
        """
        if len(pairs) == 0:
            return 0

        min = pairs[0]
        result = 0
        for i in range(1, len(pairs)):
            if pairs[i] < min:
                min = pairs[i]
                result = i

        return result

    def isConcat(self, pairs, length):
        """

        :param pairs:
        :param length:
        :return:
        >>> s = Solution()
        >>> s.isConcat([0, 3, 6], 3)
        True
        >>> s.isConcat([3, 6, 12], 3)
        False
        >>> s.isConcat([3, 5, 9], 2)
        False
        """
        pairs = sorted(pairs)
        total = len(pairs)
        for i in range(total - 1):
            if pairs[i+1] - pairs[i] != length:
                return False

        return True

    def concat(self, positions, length):
        """

        :param positions:
        :param length:
        :return:
        >>> s = Solution()
        >>> s.concat([[0, 9, 18], [3, 6, 15], [12]], 3)
        [6, 9, 12]
        """
        if len(positions) <= 1:
            return []

        result = []
        lengths = map(len, positions)
        indexs = [0] * len(positions)

        while True:
            pairs = []
            for i in range(len(positions)):
                pairs.append(positions[i][indexs[i]])
            min_position = self.minPostion(pairs)
            if self.isConcat(pairs, length):
                result.append(pairs[min_position])

            if indexs[min_position] + 1 >= lengths[min_position]:
                break
            else:
                indexs[min_position] += 1

        return result

    def optimize(self, words):
        return set(words)

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        >>> s = Solution()
        >>> s.findSubstring("barfoothefoobarman", ["bar", "foo"])
        [0, 9]
        >>> s.findSubstring("", ["abc", "bar"])
        []
        >>> s.findSubstring("foofoo", ["foo", "foo"])
        [0]
        >>> s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
        [6, 9, 12]
        >>> s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
        [8]
        >>> s.findSubstring("aabc", ["a", "a", "b"])
        [0]
        """
        if len(words) == 0:
            return []

        length = len(words[0])
        positions = []
        for word in words:
            match = []
            found = s.find(word)
            while found != -1:
                match.append(found)
                start = found + length
                found = s.find(word, start)
            if match:
                positions.append(match)

        return self.concat(positions, length)
