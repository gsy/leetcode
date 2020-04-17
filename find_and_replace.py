# -*- coding: utf-8 -*-


class Solution:
    def findReplaceString(self, string, indexes, sources, targets):
        # 排序，source， target 需要跟着 indexes 重排
        ls = [(indexes[i], sources[i], targets[i]) for i in range(len(indexes))]
        all_in_one = sorted(ls, key=lambda item: item[0])

        prev, result = 0, ""
        for index, source, target in all_in_one:
            length = len(source)
            if string[index:index+length] == source:
                # replace
                result = result + string[prev:index]
                result = result + target
                prev = index + length

        result = result + string[prev:]
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"])
    print(r)
    assert r == "eeebffff"

    r = s.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"])
    print(r)
    assert r == "eeecd"

    r = s.findReplaceString("applepie", [0, 2], ["ap", "pl"], ["ip", "hon"])
    print(r)
    assert r == "iphonepie"

    r = s.findReplaceString("vmokgggqzp", [1, 3, 5], ["mo", "kg", "ggq"], ["bfr", "s", "so"])
    print(r)
    assert r == "vbfrssozp"

    r = s.findReplaceString("vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"])
    print(r)
    assert r == "vbfrssozp"

    r = s.findReplaceString("jjievdtjfb", [1, 4, 6], ["jf", "md", "tjgb"], ["e", "foe", "oov"])
    print(r)
    assert r == "jjievdtjfb"

    # r = s.findReplaceString("jjievdtjfb", [4, 6, 1], ["md", "tjgb", "jf"], ["foe", "oov", "e"])
    # print(r)
    # assert r == "jjievdtjfb"
