import bisect


def main():
    N = int(input())
    AArr = list(map(int, input().split()))
    BArr = list(map(int, input().split()))
    CArr = list(map(int, input().split()))

    AArr.sort()
    CArr.sort()
    ans = 0
    for i in range(N):
        a = bisect.bisect_left(AArr, BArr[i])
        c = bisect.bisect_right(CArr, BArr[i])
        c = N-c
        ans += a*c

    print(ans)


if __name__ == '__main__':
    main()
