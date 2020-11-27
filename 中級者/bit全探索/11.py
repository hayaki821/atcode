def main():
    N, M = list(map(int, input().split()))
    ks = [[int(arg) for arg in input().split()] for _ in range(M)]
    p = list(map(int, input().split()))
    comb = 0

    for i in range(2**N):
        flag = False
        denki = []
        for j in range(N):

            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                denki.append(j+1)  # フラグが立っていたら num に数字を詰める
        for k in range(M):
            KS = ks[k]
            idk = KS[0]
            kosuu = 0
            for l in range(1, idk+1):
                if KS[l] in denki:
                    kosuu += 1
            if kosuu % 2 != p[k]:
                flag = False
                break
            else:
                flag = True
        if flag:
            comb += 1

    print(comb)


if __name__ == '__main__':
    main()
