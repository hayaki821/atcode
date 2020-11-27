def main():
    S = input()
    S = S[::-1]

    words = ["dream", "dreamer", "erase", "eraser"]
    words = [i[::-1] for i in words]
    ans = "NO"
    flag = True
    while True:
        for i in words:
            sub = S[:len(i)]
            if sub == i:
                if len(S) == len(i):
                    flag = True
                    S = ""
                    break
                S = S[len(i):]
                flag = True
                break
            flag = False
        if len(S) == 0:
            ans = "YES"
            break
        elif flag == False:
            break

    print(ans)


if __name__ == '__main__':
    main()
