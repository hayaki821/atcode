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
    s = S()

    if s[-1] == "s":
        ans = s+"es"
        print(ans)
    else:
        ans = s+"s"
        print(ans)


if __name__ == '__main__':
    main()
