import sys

# 첫번째 박스의 두 꼭지점 x1, y1, x2, y2
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
# 첫번째 박스의 두 꼭지점 x3, y3, x4, y4
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

if x2 < x3 or x1 > x4 or y1 > y4 or y2 < y3:
    print('NULL')
elif (x2 == x3 and y2 == y3) or (x1 == x4 and y1 == y4) or (x2 == x3 and y1 == y4) or (x1 == x4 and y2 == y3):
    print('POINT')
elif x2 == x3 or x1 == x4 or y1 == y4 or y2 == y3:
    print('LINE')
else:
    print('FACE')