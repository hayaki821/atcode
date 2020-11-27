
def main():
    N = int(input())
    fArry = [int(input()) for i in range(N)]

    now = 1
    ans = 0
    for i in range(N):
        ans += abs(fArry[i]-now)
        now = fArry[i]

    print(ans)


if __name__ == '__main__':
    main()
