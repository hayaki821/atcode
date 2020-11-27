def main():
    N = int(input())
    TXY = [[int(arg) for arg in input().split()] for _ in range(N)]
    ans = "Yes"

    T, X, Y = 0, 0, 0
    for txy in TXY:
        t1 = txy[0]
        x1 = txy[1]
        y1 = txy[2]

        dist = abs(t1-T)
        disx = abs(x1-X)
        disy = abs(y1-Y)
        if dist < disx+disy or dist % 2 != (disx+disy) % 2:
            ans = "No"
            break
        T = t1
        X = x1
        Y = y1

    print(ans)


if __name__ == '__main__':
    main()
