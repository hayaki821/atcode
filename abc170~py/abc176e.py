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
    H, W, M = LI()

    HList = [0]*H
    WList = [0]*W
    graph = set()
    for m in range(M):
        h, w = LI()
        HList[h-1] += 1
        WList[w-1] += 1
        graph.add((h-1, w-1))

    Hmax = max(HList)
    Wmax = max(WList)

    HIndex = [i for i, v in enumerate(HList) if v == Hmax]
    WIndex = [i for i, v in enumerate(WList) if v == Wmax]

    ans = Hmax + Wmax
    for h in HIndex:
        for w in WIndex:
            if not (h, w) in graph:
                print(ans)
                return

    print(ans-1)


if __name__ == '__main__':
    main()
