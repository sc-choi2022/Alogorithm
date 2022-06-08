# 현재 위치 x, y와 직사각형의 크기 w, h
x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))