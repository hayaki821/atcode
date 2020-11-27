
from itertools import product


def main():
    N, K = list(map(int, input().split()))
    a = list(map(int, input().split()))
    find = 0
    for i in range(1, N):
        if a[i-1] < a[i]:
            find += 1
    if find >= K:
        print(0)
        return

    first = a.pop(0)

    ans = float('inf')

    for bits in product((0, 1), repeat=N-1):
        build = a.copy()
        changeBuild = bits
        find = 1
        score = 0
        if sum(changeBuild) == 0:
            continue
        for i, v in enumerate(changeBuild):
            if i == 0:
                nowmax = first
            else:
                maxbuild = max(build[:i])
                nowmax = max(first, maxbuild)

            if v == 1 and nowmax >= build[i]:
                score += nowmax-build[i]+1
                build[i] = nowmax+1
            if i == 0 and first < build[i]:
                find += 1
            if i >= 1 and nowmax < build[i]:
                find += 1
        if find >= K:
            ans = min(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
