def main():
    s = input()

    dictLeet = {"A": "4", "E": "3", "G": "6",
                "I": "1", "O": "0", "S": "5", "Z": "2"}
    ans = ""
    for i in s:
        if i in dictLeet:
            ans += dictLeet[i]
        else:
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
