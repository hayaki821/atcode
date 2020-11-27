def main():
    T = list(input())

    if T[0] == "?":
        T[0] = "D"

    for i in range(1, len(T)):
        if T[i] == "?":
            T[i] = "D"

    print("".join(T))


if __name__ == '__main__':
    main()
