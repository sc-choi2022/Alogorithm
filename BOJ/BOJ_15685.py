import sys

def curve():
    di, dj = direct[d]
    ci, cj = y + di, x + dj
    dragon[ci][cj] = 1
    route = [d]

    for _ in range(g):
        for r in range(len(route)-1, -1, -1):
            go = (route[r]+1)%4
            gi, gj = direct[go]
            dragon[ci+gi][cj+gj] = 1
            ci, cj = ci+gi, cj+gj
            route.append(go)

# 드래곤 커브의 개수 N
N = int(sys.stdin.readline())
direct = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
# 드래곤 커브를 위해 사용할 배열 dragon
dragon = [[0]*101 for _ in range(101)]
# 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수 answer
answer = 0

for _ in range(N):
    # 드래곤 커브의 시작 점 (x, y), 시작 방향 d, 세대 g
    x, y, d, g = map(int, sys.stdin.readline().split())
    dragon[y][x] = 1
    curve()

for i in range(100):
    for j in range(100):
        if dragon[i][j]:
            if dragon[i][j+1] + dragon[i+1][j] + dragon[i+1][j+1] == 3:
                answer += 1

# answer 출력
print(answer)