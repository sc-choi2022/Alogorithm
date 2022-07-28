from collections import deque

# BFS
def BFS(i, j):
    # cnt를 global을 활용하여 수정할 수 있도록 한다.
    cnt = 1
    queue = deque()
    queue.append((i,j))

    while queue:
        # 시작 좌표를 si, sj로 설정
        si, sj = queue.popleft()
        # 방향을 움직여 다음 좌표 ni, nj를 구성하고
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = si + di, sj + dj
            # 위치가 범위 안이고 방문한 적없는 집이라면
            if 0<= ni < N and 0<= nj < N and arr[ni][nj] == 1:
                # queue와 visited에 좌표 값을 추가한다.
                queue.append((ni,nj))
                # 방문한 위치는 cnt를 통해 값을 변경해 준다.
                arr[ni][nj] = 0
                cnt += 1
    ans.append(cnt)

# 지도의 크기 N
N = int(input())
# 지도의 정보를 담을 리스트 arr
arr = [list(map(int, input())) for _ in range(N)]
# 정답에 대한 값들을 담아줄 리스트 ans
ans = []
# 집이 있는 위치에서 BFS를 시작하기 위한 이중 for문
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = 0
            # BFS를 집이 있는 좌표에서 시작
            BFS(i, j)

# 구역의 수를 출력
print(len(ans))
# 단지내 집의 수를 오름차순으로 출력
ans.sort()
for an in ans:
    print(an)