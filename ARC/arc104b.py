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
    Ns = input().split()

    atgc = [["A", "T"], ["C", "G"]]
    N, s = int(Ns[0]), Ns[1]

    ans = 1

    for i in range(N-1):
        t1 = s[i]
        t2 = s[i+1]
        for a in atgc:
            if (t1 == a[0] and t2 == a[1]) or (t1 == a[1] and t2 == a[0]):
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
