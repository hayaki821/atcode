# 幅優先探索（行きがけ）
import collections
import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def main():
    a = 205
    b = 82
    c = 30

    arr = []
    for i in range(31):
        for j in range(41):
            for k in range(11):
                d = a*i+b*j+c*k
                if d not in arr:
                    arr.append(d)

    print(len(arr)-1)


if __name__ == '__main__':
    main()
