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
    N, K = LI()
    flag = []
    Mod = 998244353
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(K):
        L, k = LI()
        for j in range(L, k+1):
            flag.append(j)

    flag.sort()

    for i in range(len(flag)):
        for j in range(N+1):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= Mod
            if j >= flag[i]:
                dp[i+1][j] += dp[i][j-flag[i]]
                dp[i+1][j] %= Mod

    print(dp[len(flag)][N])


if __name__ == '__main__':
    main()
