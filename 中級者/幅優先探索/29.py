# 幅優先探索（行きがけ）
import collections
import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    R, C = LI()
    sy, sx = LI()
    gy, gx = LI()

    graph = [list(S()) for _ in range(R)]

    min_dist = [[-1 for j in range(C+1)] for i in range(R+1)]  # 1_indexed
    queue = collections.deque()  # 頂点NOを入れておく

    def bfs(y, x):
        minx = x
        miny = y
        min_dist[miny][minx] = 0
        queue.append([y, x])

        while queue:
            q_NO = queue.popleft()
            q_dist = min_dist[q_NO[0]][q_NO[1]]
            if graph[q_NO[0]][q_NO[1]] == "#":
                continue
            graph[q_NO[0]][q_NO[1]] = "#"

            if graph[q_NO[0]][q_NO[1]+1] == ".":
                queue.append([q_NO[0], q_NO[1]+1])
                min_dist[q_NO[0]][q_NO[1]+1] = q_dist+1

            if graph[q_NO[0]][q_NO[1]-1] == "." and min_dist[q_NO[0]][q_NO[1]-1] == -1:
                queue.append([q_NO[0], q_NO[1]-1])
                min_dist[q_NO[0]][q_NO[1]-1] = q_dist+1

            if graph[q_NO[0]+1][q_NO[1]] == "." and min_dist[q_NO[0]+1][q_NO[1]] == -1:
                queue.append([q_NO[0]+1, q_NO[1]])
                min_dist[q_NO[0]+1][q_NO[1]] = q_dist+1

            if graph[q_NO[0]-1][q_NO[1]] == "." and min_dist[q_NO[0]-1][q_NO[1]] == -1:
                queue.append([q_NO[0]-1, q_NO[1]])
                min_dist[q_NO[0]-1][q_NO[1]] = q_dist+1

    bfs(sy-1, sx-1)

    print(min_dist[gy-1][gx-1])


if __name__ == '__main__':
    main()
