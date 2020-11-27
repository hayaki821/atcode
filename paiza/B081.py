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
    H, W = LI()
    Map = []
    hougaku = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    for _ in range(H):
        Map.append(list(S()))

    ans = 0
    for h in range(H):
        for w in range(W):
            now = Map[h][w]
            if now == '#':
                loap = 4
                for how in hougaku:
                    if h+how[1] != -1 and h+how[1] <= H-1 and w+how[0] != -1 and w+how[0] <= W-1:
                        if Map[h+how[1]][w+how[0]] == '#':
                            loap -= 1
                ans += loap

    print(ans)


if __name__ == '__main__':
    main()
