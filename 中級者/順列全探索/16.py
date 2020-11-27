
import itertools


def main():
    N = int(input())
    PArry = list(map(int, input().split()))
    QArry = list(map(int, input().split()))

    a = 0
    b = 0
    comb = [i for i in range(1, N+1)]
    for i, iter in enumerate(itertools.permutations(comb)):
        listIter = list(iter)
        if PArry == listIter:
            a = i+1
        if QArry == listIter:
            b = i+1

    print(abs(a-b))


if __name__ == '__main__':
    main()
