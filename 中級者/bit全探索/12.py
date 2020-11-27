import itertools


def main():
    N, M = list(map(int, input().split()))
    xy = [tuple(int(arg) for arg in input().split()) for _ in range(M)]
    c = 0

    if M == 0:
        print(1)
        return

    for i in range(2**N):
        flag = False
        persons = []
        for j in range(N):
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                persons.append(j+1)  # フラグが立っていたら num に数字を詰める
        comb = list(itertools.combinations(persons, 2))
        for k in comb:
            if k in xy:
                flag = True
            else:
                flag = False
                break
        if flag:
            c = max(c, len(persons))

    print(c)


if __name__ == '__main__':
    main()
