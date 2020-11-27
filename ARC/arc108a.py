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
    S, P = LI()

    ans = "No"

    for i in range(1, 10**6+1, 1):
        l = S*i-i**2
        if l <= 0:
            break
        if l == P:
            ans = "Yes"
            break

    print(ans)


if __name__ == '__main__':
    main()
