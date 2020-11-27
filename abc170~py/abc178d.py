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
    S = I()

    dp = [0]*2000
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1

    for i in range(3, S):


if __name__ == '__main__':
    main()
