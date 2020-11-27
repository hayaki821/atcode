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
    H, W = LI()
    SList = []
    SList.append(["#"]*(W+2))
    ans = 0

    for i in range(H):
        s = list(S())
        s.insert(0, "#")
        s.append("#")
        SList.append(s)

    SList.append(["#"]*(W+2))

    for i in range(1, H+1):
        for j in range(1, W+1):
            if SList[i][j] == "." and SList[i+1][j] == ".":
                ans += 1
            if SList[i][j] == "." and SList[i][j+1] == ".":
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
