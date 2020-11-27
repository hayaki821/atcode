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
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    name_roop = []

    level = 1

    ans = ""
    while N > 0:
        N -= 1
        n = N % 26
        ans += ascii_lowercase[n]
        N //= 26
    print(ans[::-1])
    # for i in range(level, 1, -1):
    #     count = 0
    #     a = 26**(i-1)
    #     for j in range(26):
    #         if N-a > 26**(i-2):
    #             N -= a
    #             count += 1
    #     name_roop.append(count)

    # name_roop.append(N)
    # for i in name_roop:
    #     ans += ascii_lowercase[i-1]
    # print(ans)


if __name__ == '__main__':
    main()
