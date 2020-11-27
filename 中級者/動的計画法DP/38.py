def main():
    q = int(input())

    for _ in range(q):
        XArry = input()
        YArry = input()

        DP = [[0] * (len(YArry)+1) for _ in range(len(XArry)+1)]  # DP[X][Y]

        for x in range(len(XArry)):
            for y in range(len(YArry)):
                if XArry[x] == YArry[y]:
                    DP[x+1][y+1] = max(DP[x][y]+1, DP[x+1][y], DP[x][y+1])
                else:
                    DP[x+1][y+1] = max(DP[x+1][y], DP[x][y+1])

        print(DP[len(XArry)][len(YArry)])


if __name__ == '__main__':
    main()
