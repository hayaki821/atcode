# 深さ優先探索（行きがけ）
import sys
from collections import deque  # 両端の配列アクセスのときは高速、それ以外はlistのままのほうがいい


def main():
    N, Q = map(int, input().split())
    tree = [deque([]) for _ in range(N)]
    value = [0]*N
    flag = [0]*N

    for _ in range(N-1):
        a, b = map(int, input().split())
        if a == b:
            continue
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    for _ in range(Q):
        p, x = map(int, input().split())
        value[p-1] += x

    stack = deque()
    stack.append(0)

    def dfs(v):
        now = v
        nowArray = tree[v]
        flag[v] = 1
        l = len(nowArray)
        for _ in range(l):  # 子ノードに値を追加
            w = tree[v].popleft()  # 子ノード
            if v not in tree[w]:
                continue
            value[w] += value[now]
            stack.append(w)

    while stack:
        top = stack.popleft()
        if flag[top] != 1:
            dfs(top)

    print(*value)


if __name__ == '__main__':
    main()
