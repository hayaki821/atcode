# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import bisect


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N, M, K = LI()
    AArray = LI()
    BArray = LI()

    aSum = [AArray[0]]
    bSum = [BArray[0]]

    cnt = 0

    for i in range(1, N):
        aSum.append(aSum[i-1]+AArray[i])
    for i in range(1, M):
        bSum.append(bSum[i-1]+BArray[i])

    for i in range(N):
        a = aSum[i]
        if a > K:
            break
        if a == K:
            cnt = max(cnt, i+1)
            break
        sa = K-a
        b = bisect.bisect_right(bSum, sa)
        cnt = max(cnt, i+1+b)

    for i in range(M):
        b = bSum[i]
        if b > K:
            break
        if b == K:
            cnt = max(cnt, i+1)
            break
        sa = K-b
        a = bisect.bisect_right(aSum, sa)
        cnt = max(cnt, i+1+a)

    print(cnt)


if __name__ == '__main__':
    main()
