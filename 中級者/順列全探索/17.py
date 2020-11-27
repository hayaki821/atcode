import itertools


def main():
    k = int(input())
    firstQuin = [[int(arg) for arg in input().split()] for _ in range(k)]
    xList = [i[0] for i in firstQuin]
    yList = [i[1] for i in firstQuin]

    combx_ = [i if i not in xList else None for i in range(8)]  # x座標８まで
    combx = [n for n in combx_ if n != None]  # 必要なx座標
    comby_ = [i if i not in yList else None for i in range(8)]  # y座標８まで
    comby = [n for n in comby_ if n != None]  # 必要なy座標

    mapFill = [["."] * (8) for _ in range(8)]

    def conflict(x, y, arrx, arry, i):
        for j in range(i+1, len(arrx)):
            x1 = arrx[j]
            y1 = arry[j]
            if x1 - y1 == x - y or x1 + y1 == x + y:
                return True
        return False

    def check(arrx, arry):
        for i in range(len(arrx)):
            x = arrx[i]
            y = arry[i]
            if conflict(x, y, arrx, arry, i):
                return False
        return True

    for i in itertools.permutations(comby, 8-k):
        xlist = combx+xList
        ylist = list(i)+yList
        if check(xlist, ylist):
            for i in range(8):  # 初期のマップ作成
                x = xlist[i]
                y = ylist[i]
                mapFill[x][y] = "Q"
            break

    for i in range(8):
        print(*mapFill[i], sep='')


if __name__ == '__main__':
    main()
