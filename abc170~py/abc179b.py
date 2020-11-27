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
    DArray = [LI() for _ in range(N)]

    ans = "No"

    for i in range(0, N-2, 1):
        if DArray[i][0] == DArray[i][1]:
            if DArray[i+1][0] == DArray[i+1][1]:
                if DArray[i+2][0] == DArray[i+2][1]:
                    ans = "Yes"
                    break

    print(ans)


if __name__ == '__main__':
    main()
