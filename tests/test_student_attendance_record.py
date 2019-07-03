# -*- coding: utf-8 -*-

from student_attendance_record import Solution


if __name__ == '__main__':
    s = Solution()
    result = s.checkRecord("PPALLP")
    print(result)
    assert result is True

    result = s.checkRecord("PPALLL")
    print(result)
    assert result is False

    result = s.checkRecord("PPAPPA")
    print(result)
    assert result is False

    result = s.checkRecord("PPAPPLLPLP")
    print(result)
    assert result is True
