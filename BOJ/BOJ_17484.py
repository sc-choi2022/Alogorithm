import sys

def dfs(ci, cj, d, add):
    global answer
    # 현재 위치의 연료 추가
    add += place[ci][cj]
    # 달에 도착했다면 answer 값 확인 후 갱신
    if ci == N-1:
        answer = min(answer, add)
        return
    # 현재 연료가 answer보다 큰 경우 return
    if add > answer:
        return

    for l in range(3):
        di, dj = direct[l]
        ni, nj = ci + di, cj + dj
        # 같은 방향으로 움직이는 경우 continue
        if l == d:
            continue
        # 다음 위치가 범위안에 존재하는 경우 dfs
        if 0 <= ni < N and 0 <= nj < M:
            dfs(ni, nj, l, add)

# 행렬의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 우주선이 그 공간을 지날 때 소모되는 연료의 양을 저장하는 배열 place
place = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 최소 연료의 값 answer
answer = float('INF')
# 우주선의 움직이는 방향을 저장하는 딕셔너리 direct
direct = {0:(1, -1), 1:(1, 0), 2:(1, 1)}

for j in range(M):
    for k in range(3):
        di, dj = direct[k]
        # 다음 위치값 ni, nj이 범위 안에 존재하는 경우
        ni, nj = di, j + dj
        if 0 <= nj < M:
            dfs(ni, nj, k, place[0][j])
# 달 여행에 필요한 최소 연료의 값을 출력
print(answer)