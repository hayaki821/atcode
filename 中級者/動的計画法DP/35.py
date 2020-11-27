def main():
    N, W = list(map(int, input().split()))
    NWArry = [list(map(int, input().split()))for _ in range(N)]

    DP = [[0] * (W+1) for _ in range(N + 1)]  # DP[N][W]

    for i in range(N):
        for j in range(0, W+1):
            if NWArry[i][1] <= j:
                DP[i+1][j] = max(DP[i][j-NWArry[i][1]]+NWArry[i][0], DP[i][j])
            else:
                DP[i+1][j] = DP[i][j]
    print(DP[N][W])


if __name__ == '__main__':
    main()
