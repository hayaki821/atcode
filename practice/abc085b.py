def main():
    N = int(input())
    dArr = list(int(input()) for _ in range(N))
    dArr = list(set(dArr))
    l = len(dArr)
    print(l)


if __name__ == '__main__':
    main()
