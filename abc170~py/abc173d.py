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
    A = LI()
    A.sort()

    maxnum = A[0]
    cnt = [1]*(maxnum+1)
    chageCnt = 0
    ans = 0
    for i in range(1, N):
        a = A[i]
        if A[i-1] == A[i]:
            cnt[a] += 1

    for i in range(N-1):
        ans += maxnum
        chageCnt += 1
        if chageCnt == cnt[maxnum]:
            maxnum = B.pop()
            chageCnt = 0

    print(ans)


if __name__ == '__main__':
    main()
