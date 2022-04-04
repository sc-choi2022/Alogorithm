# 주어진 벽의 상태에서 bfs를 진행한다.
def bfs():
    # bfs를 진행하기 위한 리스트 queue 생성
    queue = []
    # arr에 영향을 주지않고 copy하기 위해 리스트 temp 생성
    temp = []
    for ar in arr:
        temp.append(ar[:])
    # 모든 바이러스의 위치를 찾아 queue에 추가한다.
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                queue.append((i,j))
    # queue에 값이 존재하는 경우 계속 진행
    while queue:
        # queue.pop(0)의 위치값을 si, sj 변수에 할당
        si, sj = queue.pop(0)
        # 네 방향에 대해 di,dj를 활용하여 다음 위치 ni,nj를 구성한다.
        for di, dj in ((0,1), (1, 0), (0, -1), (-1,0)):
            ni = si + di
            nj = sj + dj
            # ni,nj의 위치가 범위안에 있고 temp[ni][ni]이 빈칸(0)이라면
            if  0<= ni < N and 0<= nj < M and temp[ni][nj] == 0:
                # temp[ni][nj] = 2로 저장하고 ni,nj값을 queue에 추가
                temp[ni][nj] = 2
                queue.append((ni, nj))
    # 정답 answer를 global로 호출
    global answer
    # 현재 상태에서의 0의 개수를 담을 cnt
    cnt = 0
    # temp에 0의 수를 cnt에 더한다.
    for t in temp:
        cnt += t.count(0)
    # cnt와 answer를 비교하여 큰 값을 answer에 저장한다.
    answer = max(cnt, answer)
# 벽을 3개 세우는 함수 wall
def wall(cnt):
    # 세운 벽이 3개라면 bfs()를 실행
    if cnt == 3:
        bfs()
        return
    # 위치의 값이 0인 위치를 1로 변경하고 wall을 실행
    # wall을 실행 후 다시 0으로 저장
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

# N×M인 직사각형의 길이 N, M
N, M = map(int, input().split())
# N×M인 직사각형의 정보를 담은 리스트 arr
arr = [list(map(int, input().split())) for _ in range(N)]
# answer값을 최소화
answer = 0
# 새로 새운 벽이 0일때 부터 wall을 시작
wall(0)
# answer를 출력
print(answer)