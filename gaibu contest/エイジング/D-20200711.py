# 幅優先探索（行きがけ）
import collections
import sys
import math


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    X = str(I())

    a = 0
    cnt = N-1
    for i in X:
        n = int(i)
        a += n*2**cnt
        cnt -= 1
    c = N-1
    for i in range(N):
        aa = a
        if X[0] == "0":
            aa += 2**c
        else:
            aa -= 2**c
        bin_num = int(str(aa), 2)
        print(bin_num)


if __name__ == '__main__':
    main()
