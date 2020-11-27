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
    N = I()
    ans = 0

    while True:
        if N >= 1000:
            N -= 1000
            if N == 0:
                break
        else:
            ans = 1000-N
            break

    print(ans)


if __name__ == '__main__':
    main()
