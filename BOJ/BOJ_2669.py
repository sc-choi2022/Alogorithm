blank = [[0]*100 for _ in range(100)]
area = 0

for time in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            blank[i][j] = 1

for one in blank:
    area += one.count(1)

print(area)