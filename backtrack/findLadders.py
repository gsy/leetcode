class Solution:
    def reachable(self, a, b):
        length = len(a)

        count = 0
        for i in range(length):
            if a[i] != b[i]:
                count = count + 1
            if count > 1:
                return False

        return True

    def buildMapping(self, wordList):
        # 单词之间的相互转换：
        mapping = {}
        length = len(wordList)
        for i in range(length):
            for j in range(i+1, length):
                a = wordList[i]
                b = wordList[j]
                if self.reachable(a, b):
                    if a in mapping:
                        ls = mapping.get(a)
                        ls.append(b)
                    else:
                        mapping[a] = [b]

                    if b in mapping:
                        ls = mapping.get(b)
                        ls.append(a)
                    else:
                        mapping[b] = [a]
        return mapping

    def backtrack(self, beginWord, endWord, mapping, path, result):
        if len(path) > 0 and path[-1] == endWord:
            result.append(path)

        candidates = mapping.get(beginWord, [])
        for candidate in candidates:
            if candidate not in path:
                self.backtrack(candidate, endWord, mapping, path + [candidate], result)

    def findLadders(self, beginWord, endWord, wordList):
        path, result = [], []
        if endWord not in wordList:
            return []

        mapping = self.buildMapping(wordList + [beginWord])
        self.backtrack(beginWord, endWord, mapping, path, result)

        length = None
        for ls in result:
            current = len(ls)
            if length is None:
                length = current
            elif current < length:
                length = current

        tmp = []
        for ls in result:
            current = len(ls)
            if current == length:
                new_ls = [beginWord] + ls
                if new_ls not in tmp:
                    tmp.append(new_ls)
        return tmp
