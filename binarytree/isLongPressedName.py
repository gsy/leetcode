class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        len1 = len(name)
        len2 = len(typed)
        last_char = ""
        while i < len1:
            if j >= len2:
                return False

            if name[i] == typed[j]:
                last_char = name[i]
                i = i + 1
                j = j + 1
            else:
                if last_char:
                    if typed[j] == last_char:
                        j = j+1
                    else:
                        return False
                else:
                    return False

        while j < len2:
            if typed[j] != last_char:
                return False
            else:
                j = j + 1

        return True
