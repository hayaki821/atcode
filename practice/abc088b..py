def main():
    N = int(input())
    Aarr = list(map(int, input().split()))
    Aarr.sort(reverse=True)

    a = 0
    b = 0

    for i in range(N):
        if i % 2 == 0:
            a += Aarr[i]
        else:
            b += Aarr[i]

    print(a-b)


if __name__ == '__main__':
    main()
