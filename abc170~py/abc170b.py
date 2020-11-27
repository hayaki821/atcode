# 幅優先探索（行きがけ）
import collections
import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    X, Y = LI()
    ans = "No"
    for i in range(X+1):
        for j in range(X+1):
            if i+j > X:
                break
            if 2*i+4*j == Y and i+j == X:
                ans = "Yes"
                print(ans)
                return

    print(ans)


if __name__ == '__main__':
    main()
