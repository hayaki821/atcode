def main():
    H, W, N = map(int, input().split())
    HWN = [[int(arg) for arg in input().split()] for _ in range(N)]

    mapList = [["." for _ in range(W)]for _ in range(H)]

    for i in range(N):
        block = HWN[i]
        for j in range(H):
            flag = False
            for k in range(block[2], block[2]+block[1]):
                if mapList[j][k] == "#":
                    flag = True
                    break
            if j == H-1 and flag == False:  # 一番はじめのブロック
                for h in range(block[0]):
                    for w in range(block[2], block[2]+block[1]):
                        mapList[j-h][w] = "#"
            if flag:
                for h in range(block[0]):
                    for w in range(block[2], block[2]+block[1]):
                        mapList[j-h-1][w] = "#"
                break

    for i in range(H):
        print(''.join(mapList[i]))


if __name__ == '__main__':
    main()
