# 深さ優先探索（行きがけ）
import sys
from collections import deque  # 両端の配列アクセスのときは高速、それ以外はlistのままのほうがいい


def main():

    ans = []

    def dfs(y, x):
        wh[y][x] = 0
        for dx in range(3):
            for dy in range(3):
                nx = x + dx-1
                ny = y + dy-1
                if 0 <= nx < w and 0 <= ny < h and wh[ny][nx] == 1:
                    dfs(ny, nx)

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        wh = [[int(arg) for arg in input().split()] for _ in range(h)]
        count = 0
        for i in range(w):
            for j in range(h):
                if wh[j][i] == 1:
                    dfs(j, i)
                    count += 1
        ans.append(count)

    for i in range(len(ans)):
        print(ans[i])


if __name__ == '__main__':
    main()
