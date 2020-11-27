
import numpy as np
from itertools import product


def main():
    R, C = list(map(int, input().split()))
    a = np.array([list(map(int, input().split(' '))) for _ in range(R)])
    max = R*C

    now = R*C
    for bits in product((0, 1), repeat=R):
        ban = a.copy()
        for j in range(R):
            ban[j] = a[j] ^ bits[j]
        tate = ban.sum(axis=0)
        total = np.minimum(tate, R - tate).sum()

        now = min(now, total)

    ans = max - now

    print(ans)


if __name__ == '__main__':
    main()


# def main():####遅い間に合わなかった
#     R, C = list(map(int, input().split()))
#     a = np.array([list(map(int, input().split(' '))) for _ in range(R)])
#     max = R*C

#     now = R*C
#     for i in range(2**R):
#         ban = a.copy()
#         for j in range(R):
#             if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
#                 *ban[j], = map(lambda x: (x+1) % 2, ban[j])
#         tate = ban.sum(axis=0)
#         sa = 0
#         for k in range(C):
#             if tate[k] > R/2:
#                 sa -= tate[k]
#                 sa += R-tate[k]
#         total = sum(tate)+sa

#         now = min(now, total)

#     ans = max - now

#     print(ans)


# if __name__ == '__main__':
#     main()
