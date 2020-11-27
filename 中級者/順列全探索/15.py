import math
import itertools


def main():
    N = int(input())
    xy = [list(map(int, input().split()))for _ in range(N)]
    comb = [x for x in range(N)]

    dist = 0

    for iter in itertools.permutations(comb):
        for i in range(1, N):
            dist += math.sqrt(pow(xy[iter[i-1]][0]-xy[iter[i]]
                                  [0], 2)+pow(xy[iter[i-1]][1]-xy[iter[i]][1], 2))

    dist = dist/math.factorial(N)
    print(dist)


if __name__ == '__main__':
    main()


# N = int(input())####早いやり方、forで階乗を作るやり方
# XY = [list(map(int, input().split())) for i in range(N)]
# s = 0
# import math
# for i in range(N):
#   for j in range(i+1,N):
#     s += math.sqrt((XY[i][0]-XY[j][0])**2+(XY[i][1]-XY[j][1])**2)


# ans = s*2/N
# print(ans)
