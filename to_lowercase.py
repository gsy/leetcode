# -*- coding: utf-8 -*-


class Solution:
    def toLowerCase(self, text):
        if len(text) == 0:
            return ""

        result = ""
        for char in text:
            result = result + char.lower()

        return result
