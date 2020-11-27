
def main():
    N = int(input())
    A = [int(arg) for arg in input().split()]
    ans = 1

    for i in range(N):
        if A[i] == 0:
            print(0)
            return

    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            print(-1)
            return

    print(ans)


if __name__ == '__main__':
    main()
