import datetime


def main():

    a, b, c = map(int, input().split())
    N = int(input())
    hmArray = [[int(arg) for arg in input().split()] for _ in range(N)]

    basetime = datetime.timedelta(hours=8, minutes=59)
    dt = basetime-datetime.timedelta(minutes=b)-datetime.timedelta(minutes=c)
    ans = datetime.timedelta(hours=0, minutes=0)
    for hm in hmArray:
        h = hm[0]
        m = hm[1]
        timeup = datetime.timedelta(hours=h, minutes=m)
        if timeup <= dt:
            ans = max(ans, datetime.timedelta(hours=h, minutes=m))

    ans -= datetime.timedelta(minutes=a)

    date1 = '00:00'
    d = datetime.datetime.strptime(date1, '%H:%M')
    ans = ans+d
    print("0{}:{}".format(ans.hour, ans.minute))


if __name__ == '__main__':
    main()
