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
    k, s, t = LI()
    ABC = ["ABC"]

    if k == 1:
        ans = ABC[0][s-1:t]
        print(ans)
        return

    for i in range(1, k):
        NewABC = "A"+ABC[i-1]+"B"+ABC[i-1]+"C"
        ABC.append(NewABC)

    ans = ABC[-1][s-1:t]
    print(ans)


if __name__ == '__main__':
    main()
