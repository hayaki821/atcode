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
    N, K = LI()
    pArray = LI()
    pArray.sort()

    count = 0
    for i in range(K):
        count += pArray[i]

    print(count)


if __name__ == '__main__':
    main()
