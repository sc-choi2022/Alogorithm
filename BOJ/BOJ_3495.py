import sys

# 높이 H, 너비 W
H, W = map(int, sys.stdin.readline().split())
# 다각형 polygon
polygon = [sys.stdin.readline().rstrip() for _ in range(H)]
# 넓이 area
area = 0

for i in range(H):
    line = ''
    for j in range(W):
        asc = polygon[i][j]
        if line == '' and (asc == '\\' or asc == '/'):
            line = asc
        elif line != '':
            area += 1
            if asc != '.':
                line = ''

# 다각형의 넓이를 출력
print(area)