# coding: utf-8
# Your code here!
# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import math


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N, M = LI()
    aArray = LI()
    bArray = LI()
    command = []
    checks = [0]*(N)

    ans = 'Yes'

    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

    uf = UnionFind(N)
    for _ in range(M):
        c, d = LI()
        if d < c:
            c, d = d, c
        uf.union(c-1, d-1)

    for i in range(N):
        if checks[i] == 1:
            continue
        member = uf.members(i)
        minus = 0
        puls = 0
        for m in member:
            a = aArray[m]
            b = bArray[m]
            checks[m] += 1
            sa = abs(a-b)

            if a-b > 0:
                minus += sa
            elif a-b < 0:
                puls += sa

        if minus == puls:
            continue
        else:
            ans = 'No'
            break

    print(ans)


if __name__ == '__main__':
    main()
