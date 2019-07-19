# -*- coding: utf-8 -*-


class Complex(object):
    def to_int(self, number):
        if len(number) == 0:
            return 0
        else:
            return int(number)

    def virtual_to_int(self, virtual):
        if len(virtual) == 0:
            return 0

        assert 'i' in virtual
        virtual = virtual.strip('i')
        if len(virtual) == 0:
            return 1

        return int(virtual)

    def __init__(self, string):
        real, virtual, state = '', '', "real"
        for char in string:
            if char == '+':
                state = "virtual"
                continue
            else:
                if state == "real":
                    real = real + char
                else:
                    virtual = virtual + char
        self.real = self.to_int(real)
        self.virtual = self.virtual_to_int(virtual)


class Solution:
    def multiply(self, a, b):
        real = (a.real * b.real) - (a.virtual * b.virtual)
        virtual = (a.real * b.virtual + a.virtual * b.real)
        return "{}+{}i".format(real, virtual)

    def complexNumberMultiply(self, a, b):
        return self.multiply(Complex(a), Complex(b))


if __name__ == '__main__':
    s = Solution()
    r = s.complexNumberMultiply("1+1i", "1+1i")
    assert r == "0+2i"

    r = s.complexNumberMultiply("1+-1i", "1+-1i")
    assert r == "0+-2i"

    r = s.complexNumberMultiply("1", "1")
    assert r == "1+0i"

    r = s.complexNumberMultiply("1+0i", "1")
    assert r == "1+0i"

    r = s.complexNumberMultiply("0+1i", "0+1i")
    print(r)
    assert r == "-1+0i"

    r = s.complexNumberMultiply("0+i", "0+i")
    print(r)
    assert r == "-1+0i"
