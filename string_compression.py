# -*- coding: utf-8 -*-


class Solution:
    def to_list(self, count):
        if count <= 1:
            return [""]

        result = []
        while count > 0:
            result.append(str(count % 10))
            count = int(count / 10)
        return result[::-1]

    def compress(self, chars):
        prev, count = None, 1
        tmp = []
        for char in chars + [" "]:
            if prev and char == prev:
                count = count + 1
            else:
                if count > 1:
                    tmp = tmp + self.to_list(count)
                tmp.append(char)
                prev = char
                count = 1

        for index, char in enumerate(tmp):
            if char == " ":
                break
            chars[index] = char
        # print(tmp)
        return len(tmp) - 1


if __name__ == '__main__':
    s = Solution()
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    r = s.compress(chars)
    print(r)
    print(chars)

    r = s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    print(r)

    r = s.compress(["$", "$", "$", "#", "#", "#", "#", "#", "$", "$"])
    print(r)
