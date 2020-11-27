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
    X, K, D = LI()
    X = abs(X)

    a = math.ceil(X/D)

    if K < a:
        print(abs(X-D*K))
        return
    else:
        K -= a
        X -= D*a
        if K % 2 == 0:
            print(abs(X))
            return
        else:
            print(abs(X+D))


if __name__ == '__main__':
    main()
