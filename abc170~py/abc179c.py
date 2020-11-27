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

    ans = N-1

    for i in range(2, N):
        for j in range(1, N):
            if i*j > N-1:
                break
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
