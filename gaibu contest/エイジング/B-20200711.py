# 幅優先探索（行きがけ）
import collections
import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    Aarray = LI()
    cnt = 0
    for i in range(N):
        if i % 2 == 0 and Aarray[i] % 2 != 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
