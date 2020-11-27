# 幅優先探索（行きがけ）
import collections
import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def main():

    n = I()
    ukv = [LI() for _ in range(n)]
    graph = [collections.deque([]) for _ in range(n)]

    for x in ukv:
        u, k, *v = x
        for y in v:
            graph[u-1].append(y)

    seen = [0]*(n)  # 1_indexed
    min_dist = [-1]*(n)  # 1_indexed
    queue = collections.deque()  # 頂点NOを入れておく

    def bfs():
        seen[0] = 1
        queue.append(0)
        min_dist[0] = 0
        while queue:
            q_NO = queue.popleft()
            q_dist = min_dist[q_NO]
            if not graph[q_NO]:  # もしも下に続くものがなかったときはとばす
                continue
            g = graph[q_NO]
            for _ in range(len(g)):
                g_NO = g.popleft()
                if seen[g_NO-1]:  # もしもすでに訪れていたら飛ばす
                    continue
                seen[g_NO-1] = 1
                queue.append(g_NO-1)
                min_dist[g_NO-1] = q_dist+1

    bfs()

    for i, ans in enumerate(min_dist):
        print(i+1, ans)


if __name__ == '__main__':
    main()
