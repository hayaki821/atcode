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
    PArray = LI()
    CArray = LI()

    dp = []

    ans = 0
    for i in range(N):
        check = [0]*(N)
        cnt = 0
        total = 0
        now = PArray[i]
        for j in range(K):
            if check[now-1] == 1:
                dp.append([total, cnt])
                break

            check[now-1] = 1
            now = PArray[now-1]

    for i in range(N):


if __name__ == '__main__':
    main()
