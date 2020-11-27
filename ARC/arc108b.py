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
    s = list(S())

    dp = [[0]*(N)]*(N)

    def check(a, b, c):
        if a == "f" and b == "o" and c == "x":
            return True
        return False

    x = 0
    for i in range(N-2):
        if s[i] != "f" or s[i] != "o" or s[i] != "x":
            continue
        if check(s[i], s[i+1], s[i+2]):
            x += 3
            i += 3
            continue
        if s[i] == "f":
            fList.append(i)
            continue
        if s[i] == 'o':
            oList.append(i)
            continue


if __name__ == '__main__':
    main()
