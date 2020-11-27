def main():
    N = int(input())
    Aarr = list(map(int, input().split()))
    cnt = 0
    while all(i % 2 == 0 for i in Aarr):
        Aarr = [i/2 for i in Aarr]
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
