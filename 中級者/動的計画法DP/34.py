def main():
    n = int(input())

    DP = [None] * (n + 1)  # 計算結果を保存する配列
    DP[0] = 1  # 定義より
    DP[1] = 1  # 定義より
    for i in range(2, n+1):
        DP[i] = DP[i-1] + DP[i-2]

    print(DP[n])


if __name__ == '__main__':
    main()
