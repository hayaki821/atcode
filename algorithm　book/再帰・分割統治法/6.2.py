import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def solve(i, m):
    # 整数が作れるかどうかの確認する再帰関数
    # param int,int i番目,その数字を作れるか
    # return bool
    # nは配列の個数、Aは配列
    if m == 0:  # 0になれば作れる
        return True
    if i >= n:  # n個使ってm=0にならなければ作れない
        return False
    res = solve(i+1, m) or solve(i+1, m-A[i])
    return res


def main():
    print(1)


if __name__ == '__main__':
    main()
