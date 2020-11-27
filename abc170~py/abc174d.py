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
    C = S()
    rcount = 0
    ans = 0
    for c in C:
        if c == "R":
            rcount += 1

    for r in range(rcount, N):
        if C[r] == "R":
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
