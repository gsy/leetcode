class Solution:
    def isValid(self, sub, result):
        if sub[0] == '0':
            if sub != '0':
                return False

        number = int(sub)
        if number < 0 or number > 2**31 - 1:
            return False

        length = len(result)
        if length >= 2:

            if int(result[-2]) + int(result[-1]) == number:
                return True
            else:
                return False

        return True

    def backtrack(self, text, path, result):
        # 只要找到1个就可以返回了
        length = len(text)
        if length == 0 and len(path) >= 3:
            result.append(path)
            return True

        # candidates
        for i in range(1, length+1):
            sub = text[:i]
            if self.isValid(sub, path):
                done = self.backtrack(text[i:], path + [sub], result)
                if done:
                    return True
        return False

    def splitIntoFibonacci(self, S):
        path, result = [], []
        self.backtrack(S, path, result)
        if result:
            return [int(item) for item in result[0]]
        return []
