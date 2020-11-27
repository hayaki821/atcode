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
    N, M, Q = LI()
    friends = [[0 for _ in range(N)] for _ in range(N)]
    ansList = []
    flag = [0]*(N)
    for _ in range(M):
        a, b, f = LI()
        friends[a-1][b-1] = f
        friends[b-1][a-1] = f

    max1 = 0

    for _ in range(Q):
        kigou, num = input().split(" ")
        if kigou == "+":
            flag[num-1] = 1

    print(friends)


if __name__ == '__main__':
    main()
