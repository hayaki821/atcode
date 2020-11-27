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
    A,B,C,D = LI()

    ans = "No"

    if (A<=C and C<=B) or (A<=D and D<=B) or (C<=A and A<=D) or (C<=B and B<=D):
        ans ="Yes"

    print(ans)


if __name__ == '__main__':
    main()
