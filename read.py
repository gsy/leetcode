# -*- coding: utf-8 -*-


def read(filename):
    with open(filename) as rfile:
        for line in rfile.readlines():
            print line


if __name__ == '__main__':
    read(u"/Users/guang/code/leetcode/测试/中文文件.txt")
