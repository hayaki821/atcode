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
    T = I()
    MOD = 1000000007

    for t in range(T):
        N, A, B = LI()

        pNA = (N-A+1)
        pNA = pNA**2
        pNB = (N-B+1)
        pNB = pNB**2
        minAB = max(A, B)
        ans = abs(pNA*pNB % MOD-(A**2 % MOD+B**2 % MOD-1)**2 % MOD)

        print(ans)


if __name__ == '__main__':
    main()
