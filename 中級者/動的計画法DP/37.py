def main():
    n, m = list(map(int, input().split()))
    CArry = list(map(int, input().split()))
    DP = [[0] * (n + 1) for _ in range(m + 1)]  # DP[m][n]//m枚数、ｎ円

    for i in range(0, n+1):
        DP[0][i] = 1e9
    for i in range(1, m+1):
        for j in range(0, n+1):
            if j == 0:
                DP[i][j] = 0
            elif CArry[i-1] <= j:
                DP[i][j] = min(DP[i][j-CArry[i-1]]+1, DP[i-1][j])
            else:
                DP[i][j] = DP[i-1][j]
    print(DP[m][n])


if __name__ == '__main__':
    main()
