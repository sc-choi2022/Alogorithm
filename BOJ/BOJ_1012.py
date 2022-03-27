from collections import deque
def BFS(arr):
    global cnt
    queue = deque()
    queue.append((i,j))
    visited = [(i,j)]
    while queue:
        temp = queue.popleft()
        si = temp[0]
        sj = temp[1]
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = si + di
            nj = sj + dj
            if 0<= ni < N and 0<= nj < M and arr[ni][nj] == 1:
                queue.append((ni,nj))
                visited.append((ni, nj))
                arr[ni][nj] = cnt
    cnt += 1
    ans.append(len(visited))
# 테스트 케이스 수
T = int(input())
for case in range(T):
    # 가로길이 M, 세로길이 N, 배추가 심어져 있는 위치의 개수 K
    M, N, K = map(int, input().split())
    # 배추밭의 크기 만큼의 리스트 arr
    arr = [[0]*M for _ in range(N)]
    # K개의 배추 수 만큼 배추위치를 리스트 arr에 반영
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    # 배추의 위치를 표시하기 위해 0과 1이 아닌 수를 변수 cnt에 할당
    cnt = 2
    # 모든 cnt값을 담을 리스트 ans
    ans = []
    # 배추가 있는 위치부터 BFS를 진행
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                # 첫번째 자리도 값을 cnt로 재할당
                arr[i][j] = cnt
                BFS(arr)
    # 최소의 배추흰지렁이 마리 수를 출력
    print(len(ans))