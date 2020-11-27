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
    N,M = LI()
    loadArray = [LI() for _ in range(M)]

    ans = 0

    class UnionFind():
        #クラスコンストラクタ
        #selfはインスタンス自身
        def __init__(self, n):
            #親ノードを-1に初期化する
            self.parents = [-1] * n

        #根を探す（再帰関数）
        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        #xとyの木を併合する
        def union(self, x, y):
            #x,yの根をX,Yとする
            X = self.find(x)
            Y = self.find(y) 

            #根が同じなら結合済み
            if X == Y:
                return
            #ノード数が多い方をXとする
            if self.parents[X] > self.parents[Y]:
                X, Y = Y, X

            #XにYのノード数を足す
            self.parents[X] += self.parents[Y]
            #Yの根を X>0 とする
            self.parents[Y] = X

    uf = UnionFind(N)
    for a, b in loadArray:
        #インデックスを調整し、a,bの木を結合
        a -= 1; b -= 1
        uf.union(a, b)

    for u in uf.parents:
        if u<0:
            ans += 1

    

    print(ans-1)


if __name__ == '__main__':
    main()
