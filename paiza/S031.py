# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import numpy as np


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N, C, K = LI()
    bArray = []
    for _ in range(N):
        bArray.append(LI())

    bArray.sort(key=lambda x: x[0], reverse=True)
    ans = 0
    for i in range(K-1, N):
        now = bArray[i]
        longe = now[0]
        price = now[1]
        bCopy = copy.deepcopy(bArray[:i])
        bCopy.sort(key=lambda x: x[1])
        PArray = bCopy[:K-1]
        arr = np.asarray(PArray)
        sumPrice = np.sum(arr, axis=0)[1]
        if price+sumPrice <= C:
            ans = longe
            break

    print(ans)


if __name__ == '__main__':
    main()
