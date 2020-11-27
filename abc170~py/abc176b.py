# coding: utf-8
# Your code here!
# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import math
import itertools


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()

    NStr = str(N)

    keta = 0
    for n in NStr:
        keta += int(n)

    if keta % 9 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
