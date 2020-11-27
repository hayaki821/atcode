# 幅優先探索（行きがけ）
import collections
import sys
import copy


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()

    num = 0

    for i in range(1, N+1):
        y = N//i
        num += int((y*(y+1)*i)/2)

    print(num)


if __name__ == '__main__':
    main()
