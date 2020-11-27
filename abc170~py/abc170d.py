# 幅優先探索（行きがけ）
import collections
import sys
import math
import copy
import collections


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    AArry = LI()
    AArry.sort()
    count = 0
    li = [0 for _ in range(10**6+2)]

    for i, v in enumerate(AArry):
        a = v
        if li[a] == 1:
            count += 1
        if li[a] == 0:
            if i != N-1 and AArry[i+1] == a:
                count += 1

            for j in range(a, 10**6+2, a):
                li[j] = 1

    print(N-count)


if __name__ == '__main__':
    main()
