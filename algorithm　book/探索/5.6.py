import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    n, k = LI()
    track = []
    for _ in range(n):
        v = I()
        track.append(v)
    # 最大積載量Pのk台のトラックで何個の荷物を詰めるか

    def check(P):
        i = 0  # トラックの個数
        for j in range(k):
            s = 0
            while s+track[i] <= P:

                s += track[i]
                i += 1
                if i == n:
                    return n
        return i

    def solve():
        left = 0
        right = 100000*100000
        mid = 0
        while right - left > 1:
            mid = (left+right)//2
            v = check(mid)
            if v >= n:
                right = mid
            else:
                left = mid
        return right

    ans = solve()
    print(ans)


if __name__ == '__main__':
    main()
