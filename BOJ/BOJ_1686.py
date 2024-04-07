from collections import deque
import sys

# 닭의 속도 V, 생존 가능 시간 M
V, M = map(int, sys.stdin.readline().split())
# 닭의 위치 Xs, Ys
Xs, Ys = map(float, sys.stdin.readline().split())
# 목적지의 위치 Xt, Yt
Xt, Yt = map(float, sys.stdin.readline().split())
# 벙커들의 위치를 저장하는 셋 bunkers
bunkers = set()
while True:
    try:
        tmp = sys.stdin.readline().rstrip()
        if not tmp:
            break
        bunkers.add(tuple(map(float, tmp.split())))
    except:
        break
# 넓은 범위, visit은 셋으로 설정
visit = set()

# 닭이 움질일 수 있는 최대 거리 maximum
maximum = V * M * 60
# 거리를 구하는 람다함수 length
length = lambda x1, y1, x2, y2 : ((x1-x2)**2 + (y1-y2)**2)**0.5

queue = deque([(Xs, Ys, 0)])
while queue:
    ci, cj, cnt = queue.popleft()
    if length(ci, cj, Xt, Yt) < maximum:
        print(f'Yes, visiting {cnt} other holes.')
        break
    for bunker in bunkers:
        bi, bj = bunker
        if bunker not in visit and length(ci, cj, bi, bj) < maximum:
            visit.add(bunker)
            queue.append((bi, bj, cnt+1))
else:
    print('No.')