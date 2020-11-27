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
    LArray = LI()
    ans = 0
    if N < 3:
        print(ans)
        return

    for v in list(itertools.combinations(LArray, 3)):
        v = list(v)
        v.sort()

        if v[0] == v[1] or v[2] == v[1] or v[0] == v[2]:
            continue
        elif v[0]+v[1] <= v[2]:
            continue
        else:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
