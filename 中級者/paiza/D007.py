def main():
    N = int(input())

    strs = "*"

    for _ in range(1, N):
        strs += "*"
    print(strs)


if __name__ == '__main__':
    main()
