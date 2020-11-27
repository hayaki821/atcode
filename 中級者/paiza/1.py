def main():
    array = list(map(int, input().split()))

    now = array[0]*60+array[1]
    finish = array[2]*60+array[3]

    sa = finish - now
    K = array[4]
    ans = 0
    for _ in range(int(1e15)):
        if now + K < finish:
            ans += 1
        else:
            break
        now += 1

    print(ans)


if __name__ == '__main__':
    main()
