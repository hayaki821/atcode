def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    m = list(map(int, input().split()))

    for i in range(q):
        mi = m[i]
        flag = True
        for j in range(2 ** n):
            nums = []
            for k in range(n):  # このループが一番のポイント
                if ((j >> k) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                    nums.append(A[k])  # フラグが立っていたら num に数字を詰める
            if sum(nums) == mi:
                print("yes")
                flag = False
                break
        if flag:
            print("no")


if __name__ == '__main__':
    main()
