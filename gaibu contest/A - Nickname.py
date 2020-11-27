# 幅優先探索（行きがけ）
import collections
import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    s = S()
    print(s[:3])


if __name__ == '__main__':
    main()
