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
    H, W, K = LI()
    c = []

    N = H+W
    for i in range(H):
        c.append(list(S()))

    ans = 0
    for i in range(2**N):
        cow = []
        row = []
        cCopy = copy.deepcopy(c)
        blacks = 0
        for j in range(N):
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                if j >= W:
                    row.append(j)
                else:
                    cow.append(j)
        print(cow, row)
        for h in range(H):
            if (h+W+1) in row:
                continue
            else:
                for w in range(W):
                    if w in cow:
                        continue
                    if cCopy[h][w] == "#":
                        blacks += 1

        if blacks == K:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
