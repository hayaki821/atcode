# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import numpy
import math


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    n = I()
    s = S()
    nekkures_s = list(s)
    nekkures = [int(s) for s in nekkures_s]
    res = numpy.cumsum(nekkures)
    max1 = res[-1]
    limit = max1//2

    ans = float("inf")
    if n == 3:
        ans1 = max(abs(nekkures[1]-nekkures[2]), abs(nekkures[0] -
                                                     nekkures[2]), abs(nekkures[1]-nekkures[0]))
        ans = min(ans, ans1)
        print(ans)
        return

    for i in range(n-2):
        sa = 0
        if i != 0:
            sa = res[i-1]
        start1 = res[i]-sa
        for j in range(i, n-1):
            end1 = res[j]-sa
            if end1 > limit:
                break

            for k in range(j+1, n):
                end2 = res[k] - res[j]
                end3 = max1-end1-end2

                if end2 > limit:
                    break
                ans1 = max(abs(end1-end2), abs(end3-end2), abs(end1-end3))
                ans = min(ans, ans1)

    print(ans)


if __name__ == '__main__':
    main()
