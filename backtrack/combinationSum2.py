class Solution:
    def dfs(self, candidates, target, start, end):
        print(target, start)
        if len(candidates) == 0:
            return [], False

        # target 等于 0 表明这条路径是一个解答
        if target == 0:
            return [], True

        if target < 0:
            return [], False

        result, flag = [], False
        for i in range(start, end):
            new_target = target - candidates[i]
            sub, valid = self.dfs(candidates, new_target, i+1, end)
            if valid:
                flag = True

                if sub:
                    for ls in sub:
                        ls.append(candidates[i])
                        result.append(ls)
                else:
                    result.append([candidates[i]])

        # print("result", result)
        return result, flag

    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        start = 0
        end = len(candidates)
        tmp, valid = self.dfs(candidates, target, start, end)
        if valid:
            result = []
            for ls in tmp:
                ls = sorted(ls)
                if ls not in result:
                    result.append(ls)
            return result
        return []
