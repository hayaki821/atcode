# # 幅優先探索（行きがけ）
# import collections
# import sys
# import copy
import numpy as np
from numba import njit

# def I(): return int(sys.stdin.readline().rstrip())
# def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
# def S(): return sys.stdin.readline().rstrip()
# def LS(): return list(sys.stdin.readline().rstrip().split())


# def main():
#     N, K = LI()
#     aArray = LI()

#     for i in range(K):
#         bArray = [0]*(N)
#         for j in range(N):
#             minx = max(0, j-aArray[j])
#             maxx = min(N-1, j+aArray[j])
#             bArray[minx] += 1
#             if maxx < N-1:
#                 bArray[maxx+1] -= 1
#         for k in range(N-1):
#             bArray[k+1] += bArray[k]
#         aArray = bArray
#         if sum(aArray) == N**2:
#             break

#     print(*aArray)


# if __name__ == '__main__':
#     main()
# 幅優先探索（行きがけ）


@njit
def solve(N, K, A):
    for _ in range(K):
        B = np.zeros(N + 1, dtype=np.int64)
        for i in range(N):
            a = A[i]
            B[max(0, i - a)] += 1
            B[min(N, i + a + 1)] -= 1
        A = np.cumsum(B)[:-1]  # cumsum->累積和を計算できる
        if np.all(A == N):
            return A
    return A


N, K = map(int, input().split())
A = np.array(input().split(), dtype=int)
print(' '.join(map(str, solve(N, K, A))))
