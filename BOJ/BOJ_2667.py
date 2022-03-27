from collections import deque

# BFS
def BFS(arr):
    # cnt를 global을 활용하여 수정할 수 있도록 한다.
    global cnt
    queue = deque()
    queue.append((i,j))
    visited = [(i,j)]
    while queue:
        temp = queue.popleft()
        # 시작 좌표를 si, sj로 설정
        si = temp[0]
        sj = temp[1]
        # 방향을 움직여 다음 좌표 ni, nj를 구성하고
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = si + di
            nj = sj + dj
            # 위치가 범위 안이고 방문한 적없는 집이라면
            if 0<= ni < N and 0<= nj < N and arr[ni][nj] == 1:
                # queue와 visited에 좌표 값을 추가한다.
                queue.append((ni,nj))
                visited.append((ni, nj))
                # 방문한 위치는 cnt를 통해 값을 변경해 준다.
                arr[ni][nj] = cnt
    # 한 구역 끝이나면 cnt를 1 증가하고 ans에 visited의 길이를 추가해준다.
    cnt += 1
    ans.append(len(visited))

# 지도의 크기 N
N = int(input())
# 지도의 정보를 담을 리스트 arr
arr = [list(map(int, input())) for _ in range(N)]
# 집이 있는 위치에 구역마다 구분을 위해 cnt로 값을 변경해 줄 것이다.
cnt = 2
# 정답에 대한 값들을 담아줄 리스트 ans
ans = []
# 집이 있는 위치에서 BFS를 시작하기 위한 이중 for문
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = cnt
            # BFS를 집이 있는 좌표에서 시작
            BFS(arr)
# 구역의 수를 출력
print(len(ans))
for a in range(len(ans)-1,0,-1):
    for b in range(a):
        if ans[b] > ans[b+1]:
            ans[b+1], ans[b] = ans[b], ans[b+1]
# 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력
for an in ans:
    print(an)