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
    inp = LI()

    inpSum = sum(inp)

    ans = 0

    for i in range(3):
        a = inp[0]
        b = inp[1]
        c = inp[2]
        l = [a, b, c]
        for j in range(100):
            if l[i] == 0 or l[i] == 100:
                break
            now = l[i]
            ans += now/inpSum
            l[i] += 1

    print(ans)


if __name__ == '__main__':
    main()
