def main():
    N, A, B = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        num = i
        if A <= sum([int(n) for n in str(num)]) <= B:
            ans += num
    print(ans)


if __name__ == '__main__':
    main()
