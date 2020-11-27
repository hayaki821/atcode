from math import floor, ceil
import decimal


def main():

    A, B = map(float, input().split())
    B = round(B, 2)
    A = int(A)
    A = decimal.Decimal(str(A))
    B = decimal.Decimal(str(B))
    AB = A*B
    AB = floor(AB)
    print(AB)


if __name__ == '__main__':
    main()
