import sys

# 규칙 3
def rule3():
    for r in range(len(clouds)):
        # 물이 있는 바구니의 수 cnt
        cnt = 0
        ci, cj = clouds[r]
        for di, dj in (-1, -1), (-1, 1), (1, 1), (1, -1):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and water[ni][nj]:
                cnt += 1
        water[ci][cj] += cnt

# 규칙 4
def rule4():
    newCloud = []
    for ii in range(N):
        for jj in range(N):
            if water[ii][jj] >= 2 and (ii, jj) not in clouds:
                water[ii][jj] -= 2
                newCloud.append((ii, jj))
    return newCloud

# 격자 NxN와 이동횟수 M
N, M = map(int, sys.stdin.readline().split())

# 물의 양을 담을 배열 water
water = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 숫자에 따른 방향을 담을 딕셔너리 direction
direction = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
# 구름의 위치 clouds
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
# 바구니에 들어있는 물의 양의 합 total
total = 0

for _ in range(M):
    # 방향 d, 움직이는 칸의 수 s
    d, s = map(int, sys.stdin.readline().split())

    for i in range(len(clouds)):
        dr, dc = direction[d]
        r, c = (clouds[i][0] + dr * s) % N, (clouds[i][1] + dc * s) % N
        # 1번 규칙
        clouds[i] = (r, c)
        # 2번 규칙
        water[r][c] += 1
    # 규칙3, 규칙4을 실행하는 함수 rule3, rule4
    rule3()
    clouds = rule4()

# 바구니에 들어있는 물의 양의 합 출력
for w in water:
    total += sum(w)
print(total)