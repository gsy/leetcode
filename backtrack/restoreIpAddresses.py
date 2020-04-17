class Solution:
    def backtrack(self, s, path, result):
        if len(path) == 4 and s == "":
            result.append(".".join(path))

        # 从 s 开头中截取一段，加入到 path 中
        for i in range(1, len(s) + 1):
            sub = s[:i]
            if int(sub) <= 255 and (sub == '0' or sub[0] != '0'):
                self.backtrack(s[i:], path + [sub], result)
            else:
                break

    def restoreIpAddresses(self, s):
        result, path = [], []
        if len(s) > 12:
            return []
        self.backtrack(s, path, result)
        return result
