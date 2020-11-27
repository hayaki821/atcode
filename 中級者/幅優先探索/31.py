# 幅優先探索（行きがけ）
import collections
import sys
import copy


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    six_hougaku = [[0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    W, H = LI()
    graph = [[0 for _ in range(W+2)] for _ in range(H+2)]
    tizu = [[0 for _ in range(W+2)] for _ in range(H+2)]  # 0->start
    totals = [0]*(N)

    for i in range(H):
        for j, v in enumerate(LI()):
            if v == 1:
                graph[i+1][j+1] = 1

    def bfs():
        start = [0, 0]
        min_dist = [[-1 for j in range(W+2)]
                    for i in range(H+2)]  # 1_indexed
        queue = collections.deque()  # 頂点NOを入れておく

        min_dist[start[0]][start[1]] = 0
        queue.append([start[0], start[1]])
        finsh = False
        while queue:
            q_NO = queue.popleft()
            q_dist = min_dist[q_NO[0]][q_NO[1]]
            for c in comand:
                dx = c[1]
                dy = c[0]
                if graph[q_NO[0]+dy][q_NO[1]+dx] == s_goal:
                    totals[i] = q_dist+1
                    finsh = True
                    break
                if graph[q_NO[0]+dy][q_NO[1]+dx] != "X" and min_dist[q_NO[0]+dy][q_NO[1]+dx] == -1:
                    queue.append([q_NO[0]+dy, q_NO[1]+dx])
                    min_dist[q_NO[0]+dy][q_NO[1]+dx] = q_dist+1
            if finsh:
                break

    bfs()

    print(sum(totals))


if __name__ == '__main__':
    main()

