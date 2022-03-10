K = int(input())

x = 0
y = 0
x_set = {x}
y_set = {y}

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

for i in range(5):
    d, length = map(int, input().split())
    x_set.add(dx[d]*length)
    y_set.add(dy[d]*length)
    if i == 4:
        last = []

x_set = list(x_set)
y_set = list(y_set)
x_set.sort()
y_set.sort()

area = x_set[-1]*x_set[-1] -