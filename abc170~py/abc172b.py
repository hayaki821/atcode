# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    S1 = S()
    T = S()

    cnt = 0

    for i, s in enumerate(S1):
        if T[i] != s:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
