def main():
    m = int(input())
    *M, = [tuple(map(int, input().split())) for _ in range(m)]
    n = int(input())
    *N, = [tuple(map(int, input().split())) for _ in range(n)]
    set_N = set(N)

    mx = M[0][0]
    my = M[0][1]
    flag = True
    x = 0
    y = 0
    for i in range(n):
        sax = N[i][0]-mx
        say = N[i][1]-my
        for j in range(1, m):
            flag = True
            movex = M[j][0]+sax
            movey = M[j][1]+say
            if (movex, movey) not in set_N:
                flag = False
                break
        if flag:
            x = sax
            y = say
            break

    print(x, y)


if __name__ == '__main__':
    main()
