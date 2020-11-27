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
    Si = [0]*(4)
    s = ["AC", "WA", "TLE", "RE"]
    for _ in range(N):
        a = S()
        for j, ss in enumerate(s):
            if a == ss:
                Si[j] += 1
                break

    print("AC x " + str(Si[0]))
    print("WA x " + str(Si[1]))
    print("TLE x " + str(Si[2]))
    print("RE x " + str(Si[3]))


if __name__ == '__main__':
    main()
