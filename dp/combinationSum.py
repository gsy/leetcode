class Solution:
    def getCombination(self, candidates, target, cached):
        # 递归地找
        if len(candidates) == 0:
            return []

        if target < candidates[0]:
            return []

        result = []
        if target in candidates:
            result.append([target])

        for candidate in candidates:
            remain = target - candidate

            if remain >= candidates[0]:
                subA = []
                subB = []
                if remain in cached:
                    subA = cached[remain]
                else:
                    subA = self.getCombination(candidates, remain, cached)

                if candidate in cached:
                    subB = cached[candidate]
                else:
                    subB = self.getCombination(candidates, candidate, cached)

                if subA and subB:
                    for lsA in subA:
                        for lsB in subB:
                            tmp = sorted(lsA + lsB)
                            if tmp not in result:
                                result.append(tmp)

        cached[target] = result
        # print(target, result, cached)
        return result

    def combinationSum(self, candidates, target):
        cached = {}
        candidates = sorted(candidates)
        result = self.getCombination(candidates, target, cached)
        return result
