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
    A, B, C = LI()
    K = I()
    for i in range(K):
        if A >= B:
            B *= 2
        else:
            if B >= C:
                C *= 2
            else:
                break

    if A < B and B < C:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
