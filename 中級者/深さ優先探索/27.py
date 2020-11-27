# 深さ優先探索（行きがけ）
import sys
from collections import deque  # 両端の配列アクセスのときは高速、それ以外はlistのままのほうがいい

maxDenpth = 0


def main():
    m = int(input())
    n = int(input())
    mn = [[int(arg) for arg in input().split()] for _ in range(n)]
    maplist = [[0 for _ in range(m+2)]for _ in range(n+2)]

    for i in range(n+2):
        for j in range(m+2):
            if i == 0 or j == 0 or i == n+1 or j == m+1:
                continue
            maplist[i][j] = mn[i-1][j-1]

    def dfs(maplist, x, y, depth):
        global maxDenpth
        mapx = x+1
        mapy = y+1
        maplist[mapx][mapy] = 0
        if maplist[mapx+1][mapy] == 1:
            dfs(maplist, x+1, y, depth+1)
        if maplist[mapx-1][mapy] == 1:
            dfs(maplist, x-1, y, depth+1)
        if maplist[mapx][mapy+1] == 1:
            dfs(maplist, x, y+1, depth+1)
        if maplist[mapx][mapy-1] == 1:
            dfs(maplist, x, y-1, depth+1)

        maplist[mapx][mapy] = 1  # 帰ってくるときにもとに戻す
        if maplist[mapx][mapy-1] == 0 and maplist[mapx][mapy+1] == 0 and maplist[mapx+1][mapy] == 0 and maplist[mapx-1][mapy] == 0:
            if depth+1 > maxDenpth:
                maxDenpth = depth+1
            return

    for i in range(n):
        for j in range(m):
            if mn[i][j] != 1:
                continue
            dfs(maplist, i, j, 0)

    print(maxDenpth)


if __name__ == '__main__':
    main()
