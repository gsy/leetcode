class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        mode = ""
        for i, char in enumerate(word):
            if i == 0:
                if char.isupper():
                    mode = "capital"
                else:
                    mode = "lower"
            else:
                if char.isupper():
                    if mode == "capital":
                        if i == 1:
                            mode = "upper"
                        else:
                            return False
                    elif mode == "lower":
                        return False
                else:
                    if mode == "upper":
                        return False

        return True
