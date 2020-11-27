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
    N, M = LI()
    friendsList = [[] for _ in range(N)]
    friendsFlag = [0]*(N)
    group = 0

    for i in range(M):
        A, B = LI()
        if friendsList[A-1] not in B-1:
            friendsList[A-1].append(B-1)
        if friendsList[B-1] not in A-1:
            friendsList[B-1].append(A-1)


if __name__ == '__main__':
    main()
