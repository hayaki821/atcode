from collections import defaultdict


def main():
    H, W = map(int, input().split())
    Aarray = [[int(arg) for arg in input().split()] for _ in range(2)]

    mapFill = [[0] * (W) for _ in range(H)]

    mapFill[0][0] = Aarray[0][0]
    mapFill[0][1] = Aarray[0][1]
    mapFill[1][0] = Aarray[1][0]
    mapFill[1][1] = Aarray[1][1]
    for i in range(H):
        for j in range(W):
            if (i == 0 and j == 0) or (i == 1 and j == 0) or (i == 0 and j == 1) or (i == 1 and j == 1):
                continue
            if i == 0 or i == 1:
                mapFill[i][j] = mapFill[i][j-1]+(mapFill[i][1]-mapFill[i][0])
            else:
                mapFill[i][j] = mapFill[i-1][j]+(mapFill[1][j]-mapFill[0][j])

    for i in range(H):
        print(*mapFill[i])


if __name__ == '__main__':
    main()

# preset = input()
# height = int(preset.split()[0])
# width = int(preset.split()[1])
# position = [input() for i in range(2)]

# column1_case = int(position[1].split()[0]) - int(position[0].split()[0])
# column1_1 = int(position[0].split()[0])
# column1 = [column1_1 + i * column1_case for i in range(height)]

# column2_case = int(position[1].split()[1]) - int(position[0].split()[1])
# column2_1 = int(position[0].split()[1])
# column2 = [column2_1 + i * column2_case for i in range(height)]

# row_all = []

# for rows in range(height):
#     row1_case = column2[rows] - column1[rows]
#     row1_1 = column1[rows]
#     row1 = [row1_1 + i * row1_case for i in range(width)]
#     # print(row1)
#     print(' '.join(map(str, row1)))
