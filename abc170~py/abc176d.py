# coding: utf-8
# Your code here!
# 幅優先探索（行きがけ）
import collections
import sys
import copy
import re
import math
import itertools


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    H, W = LI()
    Ch, Cw = LI()
    Dh, Dw = LI()
    graph = [collections.deque(["#", "#"]) for _ in range(H+4)]
    for i in range(H+4):
        if i == 0 or i == H+2 or i == 1 or i == H+3:
            graph[i] = ["#"]*(W+4)
        else:
            for v in S():
                graph[i] += [v]
            graph[i] += ["#",  "#"]
    print(graph)

    queue = collections.deque()  # 頂点NOを入れておく


if __name__ == '__main__':
    main()
