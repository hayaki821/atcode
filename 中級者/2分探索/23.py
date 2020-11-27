from itertools import combinations
from bisect import bisect_right


# def main():
#     N, M = list(map(int, input().split(' ')))
#     P = [0] + [int(input()) for _ in range(N)]
#     PP = [sum(c) for c in combinations(P, 2)]
#     PP.sort()
#     ans = 0
#     for pp in PP:
#         s = pp + PP[bisect_right(PP, M - pp) - 1]
#         if s <= M:
#             ans = max([ans, s])
#     print(ans)


# if __name__ == '__main__':
#     main()


def main():
    N, M = list(map(int, input().split(" ")))
    P = [0]+[int(input()) for _ in range(N)]
    PP = [sum(c) for c in combinations(P, 2)]
    PP.sort()
    ans = 0
    for pp in PP:
        s = pp+PP[bisect_right(PP, M-pp)-1]
        if(s > M):
            continue
        else:
            ans = max([ans, s])

    print(ans)


if __name__ == '__main__':
    main()
