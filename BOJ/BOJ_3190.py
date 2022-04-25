from collections import deque

# NxN의 길이 N
N = int(input())
# NxN 행렬의 상태를 표현할 리스트 arr
arr = [[0]*N for _ in range(N)]
# 사과의 개수 K
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    # 사과의 위치에 'A'를 저장한다.
    arr[i-1][j-1] = 'A'

# 방향이 변하는 횟수 L
L = int(input())
# 방향변경 정보를 key, value로 저장할 딕셔너리 change
change = {}
for _ in range(L):
    # X초, 방향 C
    X, C = input().split()
    # X초 후에 바꿀 방향 C를 X:C로 change에 저장
    change[int(X)] = C

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
d = 0 # 뱀은 처음에 오른쪽을 향한다.

# 뱀이 있는 위치를 담을 deque snack
snake = deque()
# 초기 위치 (0,0)을 저장
snake.append((0,0))
# 뱀이 있는 위치에 1을 할당
arr[0][0] = 1
cnt = 0 # 시간을 카운트하는 변수 cnt
# 현재 위치 ni, nj
ni, nj = 0, 0
while True:
    cnt += 1    # 시간 cnt 1증가
    # 방향에 따라 움직인 다음위치를 ni에 저장
    ni = ni + di[d]
    nj = nj + dj[d]
    # ni,nj가 범위 안에 있고 arr[ni][nj]이 이미 뱀이 위치해있지 않다면
    if 0<= ni <N and 0<= nj <N and arr[ni][nj] != 1:
        # snake에 현 위치를 추가하고 위치 값에 1을 저장
        snake.append((ni, nj))
        arr[ni][nj] = 1
        if arr[ni][nj] == 0:
            # 꼬리의 위치 pi, pj
            pi, pj = snake.popleft()
            # pi, pj의 값을 다시 0으로 저장
            arr[pi][pj] = 0
        # 현재 시간이 방향을 변경하는 시간에 속한다면
        if cnt in change.keys():
            # cnt를 key로 value를 확인하여 d를 재할당
            if change[cnt] == 'L':
                d = (d-1)%4
            elif change[cnt] == 'D':
                d = (d+1)%4
    # 종료 조건에 도달하면 while문 탈출
    else:
        break
# cnt를 출력
print(cnt)