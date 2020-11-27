from collections import defaultdict


def main():
    N = int(input())
    aArray = list(map(int, input().split()))

    DP = [defaultdict(int) for _ in range(N-1)]  # DP[X][Y]
    DP[0][aArray[0]] = 1
    for i in range(1, N-1):
        for j in range(21):
            if 0 <= j+aArray[i] <= 20:
                DP[i][j] += DP[i-1][j+aArray[i]]
            if 0 <= j-aArray[i] <= 20:
                DP[i][j] += DP[i-1][j-aArray[i]]

    print(DP[N-2][aArray[N-1]])


if __name__ == '__main__':
    main()
