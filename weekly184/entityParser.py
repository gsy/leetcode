class Solution:
    def entityParser(self, text: str) -> str:
        tokens = text.split(' ')
        result = []
        special = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        result = []
        for token in tokens:
            if token in special:
                result.append(special[token])
            else:
                # 替换字符串,
                tmp = token
                for key, value in special.items():
                    tmp = tmp.replace(key, value)
                result.append(tmp)
        # print(result)
        return " ".join(result)
