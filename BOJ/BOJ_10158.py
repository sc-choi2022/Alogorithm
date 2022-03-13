# 가로 w 세로 h
w, h = map(int,input().split())
# 개미의 첫 위치
p, q = map(int,input().split())
# 시간
t = int(input())

pt = (p + t) % (2 * w)
qt = (q + t) % (2 * h)

if pt > w:
    x = 2*w -pt
else:
    x = pt
if qt > h:
    y = 2*h -qt
else:
    y = qt

print(x, y)