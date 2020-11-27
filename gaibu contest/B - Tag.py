# 幅優先探索（行きがけ）
import collections
import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    A, V = LI()
    B, W = LI()
    T = I()

    if A <= B:
        a = A+V*T
        b = B+W*T
        if a >= b:
            print("YES")
        else:
            print("NO")
    else:
        a = A-V*T
        b = B-W*T
        if a <= b:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
