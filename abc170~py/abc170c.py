# 幅優先探索（行きがけ）
import collections
import sys
import math


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    X, N = LI()
    PArry = LI()
    ans = float("inf")
    sa = float("inf")
    for i in range(-N, N+1):
        a = X+i
        if a in PArry:
            continue
        s = abs(X-a)
        if sa == s:
            ans = min(ans, a)
        if s < sa:
            ans = a
            sa = s

    print(ans)


if __name__ == '__main__':
    main()
