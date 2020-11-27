# coding: utf-8
# Your code here!
# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import math


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    if 400 <= N and N <= 599:
        print(8)
        return
    if 600 <= N and N <= 799:
        print(7)
        return
    if 800 <= N and N <= 999:
        print(6)
        return
    if 1000 <= N and N <= 1199:
        print(5)
        return
    if 1200 <= N and N <= 1399:
        print(4)
        return
    if 1400 <= N and N <= 1599:
        print(3)
        return
    if 1600 <= N and N <= 1799:
        print(2)
        return
    if 1800 <= N and N <= 1999:
        print(1)
        return


if __name__ == '__main__':
    main()
