# coding: utf-8
# Your code here!
# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import math
import bisect


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    pArray = LI()
    numList = [-1]*(200002)

    ans = 0

    for p in pArray:
        numList[p] = 1
        for i in range(ans, N+1):
            if numList[i] == -1:
                ans = i
                break
        print(ans)


if __name__ == '__main__':
    main()
