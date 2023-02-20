import sys

# 첫번째 박스의 두 꼭지점 x1, y1, x2, y2
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
# 첫번째 박스의 두 꼭지점 x3, y3, x4, y4
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
box1 = ((x1, y1), (x1, y2), (x2, y1), (x2, y2))
box2 = ((x3, y3), (x3, y4), (x4, y3), (x4, y4))

for b1 in box1:
    if b1 in box2:
        print('POINT')
        break

if x1 == x3 or x1 == x4 or x2 == x3 or x2 == x4 or y1 == y3 or y1 == y4 or y2 == y3 or y2 == y4:
    print('LINE')