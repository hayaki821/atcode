def main():
    a = int(input())
    b, c = map(int, input().split(" "))
    s = input()
    num = a+b+c

    print("{} {}".format(num, s))


if __name__ == '__main__':
    main()
