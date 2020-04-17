# -*- coding: utf-8 -*-


class Solution:
    def camelMatch(self, queries, pattern):
        result = []
        for query in queries:
            if self.match(query, pattern):
                result.append(True)
            else:
                result.append(False)
        return result

    def is_upper(self, char):
        return char.isupper()

    def is_lower(self, char):
        return char.islower()

    def match(self, query, pattern):
        if len(pattern) == 0 or len(query) == 0:
            return False

        pattern_generator = (char for char in pattern)
        query_generator = (char for char in query)

        pchar = next(pattern_generator)
        qchar = next(query_generator)
        matched = False

        while True:
            try:
                if self.is_upper(pchar) and self.is_upper(qchar):
                    if pchar == qchar:
                        matched = True
                        qchar = next(query_generator)
                        pchar = next(pattern_generator)
                    else:
                        return False

                if self.is_upper(pchar) and self.is_lower(qchar):
                    matched = False
                    qchar = next(query_generator)

                if self.is_lower(pchar) and self.is_upper(qchar):
                    return False

                if self.is_lower(pchar) and self.is_lower(qchar):
                    if pchar != qchar:
                        matched = False
                        qchar = next(query_generator)
                    else:
                        matched = True
                        qchar = next(query_generator)
                        pchar = next(pattern_generator)
            except StopIteration:
                pattern_left = list(pattern_generator)
                query_left = list(query_generator)
                # print(pattern_left, query_left)
                if len(pattern_left) > 0:
                    return False
                return all([char.islower() for char in query_left]) and matched
