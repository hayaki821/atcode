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

    ans = "-1"

    for i in range(1, N):
        a = 3**i
        a5 = 5**i
        if a > N and a5 > N:
            break
        for j in range(1, N):
            b = 5**j
            b3 = 3**j
            ab = a+b
            a5b3 = a5+b3
            if ab > N and a5b3 > N:
                break
            elif ab == N:
                ans = str(i)+" "+str(j)
                print(ans)
                return
            elif a5b3 == N:
                ans = str(j)+" "+str(i)
                print(ans)
                return

    print(ans)


if __name__ == '__main__':
    main()
