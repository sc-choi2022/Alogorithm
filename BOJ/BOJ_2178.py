from collections import deque
# nxm 크기의 미로
n, m = map(int, input().split())
# arr nxm의 미로에 대한 정보를 담을 리스트 arr
arr = [list(map(int, input())) for _ in range(n)]
# deque를 활용하여 변수 queue 생성
queue = deque()
# 방향에 대한 정보 di, dj
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 첫 번째 위치를 queue에 추가
queue.append((0, 0))

# queue가 비어있지 않을 때 계속
while queue:
    # temp는 queue의 가장 처음 값
    temp = queue.popleft()
    # temp의 위치를 i, j로 설정
    i = temp[0]
    j = temp[1]
    # 모든 방향에 대해 BFS를 할 것이기 때문에 break를 사용하지 않는다.
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        # 범위 안에 있고 그 값이 1이라면 queue에 추가하고 i,j의 위치의 값에 +1 한 값을 할당
        if 0<= ni < n and 0<= nj < m and arr[ni][nj] == 1:
            queue.append((ni, nj))
            arr[ni][nj] = arr[i][j] + 1
# 도착 위치의 값을 출력, BFS이기 때문에 최단거리가 이미 도착했을 것!
print(arr[n-1][m-1])