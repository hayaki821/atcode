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
    si = S()
    ans = 0
    for i, s in enumerate(si):
        if s == "R":
            if ans > 0 and si[i-1] == "R":
                ans += 1
            elif ans == 0:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
