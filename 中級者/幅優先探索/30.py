# 幅優先探索（行きがけ）
import collections
import sys
import copy


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    comand = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    H, W, N = LI()
    graph = [["X"] for _ in range(H+2)]
    tizu = [[] for i in range(N+1)]  # 0->start
    totals = [0]*(N)

    for i in range(H+2):
        if i == 0 or i == H+1:
            graph[i] = ["X"]*(W+2)
        else:
            for j, v in enumerate(S()):
                if v == "S":
                    tizu[0] = [i, j+1]
                elif v != "." and v != "X":
                    v = int(v)
                    tizu[v] = [i, j+1]
                graph[i] += [v]
            graph[i] += ["X"]

    def bfs():
        for i in range(N):
            min_dist = [[-1 for j in range(W+2)]
                        for i in range(H+2)]  # 1_indexed
            queue = collections.deque()  # 頂点NOを入れておく
            start = tizu[i]
            s_goal = i+1
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
