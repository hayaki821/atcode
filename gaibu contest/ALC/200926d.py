# coding: utf-8
# Your code here!
# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import math
from bisect import bisect_left

def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N,K = LI()
    seq = []
    dp = [float("inf")]*(N)

    for _ in range(N):
        seq.append(I())

    LIS = [seq[0]]

    for i in range(len(seq)):
        if abs(seq[i]-LIS[-1])<=K:
            LIS.append(seq[i])
        else:
            LIS[bisect_left(LIS, seq[i])] = seq[i]


    print(len(LIS))


if __name__ == '__main__':
    main()
