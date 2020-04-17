# -*- coding: utf-8 -*-


class Solution:
    def compare(self, version1, version2):
        if version1 is None and version2 is None:
            return 0
        elif version1 is None:
            return -1 if int(version2) > 0 else 0
        elif version2 is None:
            return 1 if int(version1) > 0 else 0

        version1 = int(version1)
        version2 = int(version2)
        if version1 == version2:
            return 0
        elif version1 > version2:
            return 1
        else:
            return -1

    def compareVersion(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')

        length1 = len(version1)
        length2 = len(version2)
        length = max(length1, length2)
        for index in range(length):
            v1 = version1[index] if index < length1 else None
            v2 = version2[index] if index < length2 else None
            result = self.compare(v1, v2)
            if result != 0:
                return result
        return 0


if __name__ == '__main__':
    s = Solution()
    r = s.compareVersion("1.0", "2.0")
    assert r == -1

    r = s.compareVersion("1.0", "1.0.0")
    assert r == 0

    r = s.compareVersion("1.0", "1.0.01")
    assert r == -1

    r = s.compareVersion("1.0.0", "1.0.01")
    assert r == -1

    r = s.compareVersion("1.0.1", "1.0.01")
    assert r == 0

    r = s.compareVersion("1.0.1", "1.0.0.1")
    assert r == 1

    r = s.compareVersion("1.0.0", "1.0.0.1")
    assert r == -1
