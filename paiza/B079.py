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
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    s, t = LS()
    sArray = []
    tArray = []
    now = []
    now2 = []
    for i in s:
        idx = alphabet.index(i)
        sArray.append(idx+1)
    for i in t:
        idx = alphabet.index(i)
        tArray.append(idx+1)
    now = sArray+tArray
    now2 = tArray+sArray

    while len(now) > 1:
        n = []
        n2 = []
        for i in range(len(now)-1):
            a = now[i]+now[i+1]
            b = now2[i]+now2[i+1]
            if a > 101:
                a -= 101
            if b > 101:
                b -= 101
            n.append(a)
            n2.append(b)
        now = n
        now2 = n2
    print(max(now[0], now2[0]))


if __name__ == '__main__':
    main()
