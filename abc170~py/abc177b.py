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
    S1 = S()
    T = S()

    ans = float("inf")

    for i in range(0, len(S1)):
        if i == len(S1)-len(T):
            break
        count = 0
        for j in range(len(T)):
            s = S1[i+j]
            t = T[j]
            if s != t:
                count += 1
        ans = min(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
