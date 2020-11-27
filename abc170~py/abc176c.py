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
    AArray = LI()
    ans = 0
    max_sintyou = 0

    for A in AArray:
        if max_sintyou > A:
            sa = max_sintyou-A
            ans += sa
            A += sa

        max_sintyou = max(A, max_sintyou)
    print(ans)


if __name__ == '__main__':
    main()
