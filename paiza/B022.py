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
    M, N, K = LI()
    enzetu = [0]*M

    for _ in range(K):
        a = I()-1
        if N > 0:
            enzetu[a] += 1
            N -= 1
        for i in range(M):
            if a != i and enzetu[i] > 0:
                enzetu[i] -= 1
                enzetu[a] += 1

    ans = [i for i, v in enumerate(enzetu) if v == max(enzetu)]

    for a in ans:
        print(a+1)


if __name__ == '__main__':
    main()
