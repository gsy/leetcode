__author__ = 'guang'

class Solution(object):
    def compare_version_by_level(self, version1, version2):
        if len(version1) == len(version2) == 0:
            return 0
        elif len(version1) == 0:
            return -1
        elif len(version2) == 0:
            return 1
        else:
            v1 = version1[0]
            v2 = version2[0]
            if int(v1) > int(v2):
                return 1
            elif int(v1) < int(v2):
                return -1
            else:
                return self.compare_version_by_level(version1[1:], version2[1:])

    def unpack_version(self, version):
        """
        >>> s = Solution()
        >>> s.unpack_version("1.0")
        ['1']
        >>> s.unpack_version("0")
        []
        """
        result = version.split('.')
        while result and int(result[-1]) == 0:
            result.pop(-1)

        return result

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        >>> s = Solution()
        >>> s.compareVersion('0.1', '1.1')
        -1
        >>> s.compareVersion('1.1', '1.1')
        0
        >>> s.compareVersion('1.2', '1.1')
        1
        >>> s.compareVersion('1.2', '13.37')
        -1
        >>> s.compareVersion('0.1', '0.0.1')
        1
        >>> s.compareVersion('1', '1.0')
        0
        >>> s.compareVersion('1', '0')
        1
        >>> s.compareVersion("19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000", "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000")
        0
        """
        return self.compare_version_by_level(self.unpack_version(version1), self.unpack_version(version2))


