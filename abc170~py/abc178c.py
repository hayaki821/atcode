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

    a = 1

    if N == 1:
        print(0)
        return
    elif N == 2:
        print(2)
        return
    else:
        for i in range(1, N-1):
            a *= 10
            a %= (10**9+7)

        a *= 10
        a %= (10**9+7)
        print(a)


if __name__ == '__main__':
    main()
