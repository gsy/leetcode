class Solution:
    def compare(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)

        for i in range(min(len1, len2)):
            if word1[i] > word2[i]:
                return 1
            elif word1[i] < word2[i]:
                return -1

        if len1 == len2:
            return 0
        elif len1 > len2:
            return 1
        else:
            return -1

    def findString(self, words, s):
        length = len(words)

        left, right = 0, length-1
        while left <= right:
            mid = (left + right) // 2

            while words[mid] == "" and mid > left:
                mid = mid - 1

            tmp = self.compare(words[mid], s)
            if tmp == 0:
                return mid
            elif tmp > 0:
                right = mid - 1
            else:
                left = mid + 1

        return -1
