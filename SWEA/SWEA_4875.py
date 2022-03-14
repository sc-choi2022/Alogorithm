import sys
sys.stdin = open('sample_input.txt')
# 테스트 케이스
T = int(input())
# 방향을 정해주는 값을 담은 di, dj
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for case in range(1, T+1):
    # NxN 행렬의 N
    N = int(input())
    # NxN 행렬을 담을 리스트 arr
    arr = [list(map(int, input())) for _ in range(N)]
    # stack과 visited 값 초기화
    stack = []
    visited = []

    # 시작 위치를 찾는 for문
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 2:
                # 시작 위치를 찾았다면 stack과 visited에 추가
                stack.append([a, b])
                visited.append([a, b])
                break
    # ans값 초기화
    ans = 0
    # stack이 비어있지 않으면 계속
    while stack:
        # stack의 top의 값을 변수 top에 할당
        top = stack[-1]
        # 네 방향으로 현재 위치를 옮긴다
        for d in range(4):
            i = top[0] + di[d]
            j = top[1] + dj[d]
            # 범위안에 있고 위치에 값이 0이고 방문한 적이 없다면 stack과 visited에 추가
            if 0<= i < N and 0<= j < N and arr[i][j] == 0 and [i, j] not in visited:
                stack.append([i, j])
                visited.append([i, j])
                break
            # 범위 안에 있고 위치 값이 3이면 ans에 1 할당
            elif 0<= i < N and 0 <= j < N and arr[i][j] == 3:
                ans = 1
                break
        # 만약 for문에서 break를 만나지 못했다면
        else:
            stack.pop()
        # 이미 도달했다면 while문 탈출
        if ans == 1:
            break
    # 테스트케이스 번호와 정답 출력
    print(f'#{case} {ans}')