def main():
    N = int(input())
    AArry = [input() for i in range(N)]

    for i in range(N):

        a = AArry[i]

        if a[-1] == "s" or a[-1] == "o" or a[-1] == "x":
            a += "es"
        elif a[-1] == "h" and (a[-2] == "s" or a[-2] == "c"):
            a += "es"
        elif a[-1] == "f":
            a = a.rstrip("f")
            a += "ves"
        elif a[-1] == "e" and a[-2] == "f":
            a = a.rstrip("e")
            a = a.rstrip("f")
            a += "ves"
        elif a[-1] == "y" and (a[-2] != "a" and a[-2] != "i" and a[-2] != "u" and a[-2] != "e" and a[-2] != "o"):
            a = a.rstrip("y")
            a += "ies"
        else:
            a += "s"
        print(a)


if __name__ == '__main__':
    main()
