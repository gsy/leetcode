# -*- coding: utf-8 -*-

class Solution:
    def replaceWords(self, dictionary, sentence):
        mapping = {}
        for word in dictionary:
            first_char = word[0]
            ls = mapping.get(first_char, [])
            ls.append(word)
            mapping[first_char] = sorted(ls, key=len)

        # print(mapping)
        result = []
        for word in sentence.split(" "):
            if len(word) == 0:
                continue
            first_char = word[0]
            matched = False
            if first_char in mapping:
                candidates = mapping[first_char]
                for candidate in candidates:
                    if word.startswith(candidate):
                        result.append(candidate)
                        matched = True
                        break
            if not matched:
                result.append(word)
        return " ".join(result)

if __name__ == "__main__":
    s = Solution()
    r = s.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
    print(r)
    assert r == "the cat was rat by the bat"
