# -*- coding: utf-8 -*-


class Solution:
    def checkRecord(self, s):
        absent_count = 0
        late_count = 0

        for char in s:
            if char == 'L':
                late_count = late_count + 1
                if late_count > 2:
                    return False
            elif char == 'A':
                late_count = 0
                absent_count = absent_count + 1
                if absent_count > 1:
                    return False
            else:
                late_count = 0

        return True
