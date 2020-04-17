class Solution:
    def processQueries(self, queries, m):
        ls = [i for i in range(1, m+1)]
        result = []
        for query in queries:
            left, right = [], []
            for i, num in enumerate(ls):
                if num != query:
                    left.append(num)
                else:
                    result.append(i)
                    right = ls[i+1:]
                    break
            ls = [query] + left + right
        return result
