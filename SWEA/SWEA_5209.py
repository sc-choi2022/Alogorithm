def DFS(n):
    global add, answer
    if n == N:
        if answer > add:
            answer = add
        return

    if answer <= add:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            add += arr[n][i]
            DFS(n+1)
            visited[i] = 0
            add -= arr[n][i]

T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    add = 0
    answer = 99 * 15
    visited = [0]*N

    DFS(0)
    print(f'#{case} {answer}')

def dfs(n, lst):
    global ans, add
    # N개의 공장에 방문하기 전에 이전 값보다 크면 return
    if add >= ans:
        return
    # N개의 공장에 대한 정보가 다 모였다면
    if n == N:
        # 합을 저장할 변수 temp 초기화
        temp = 0
        # N개의 정보에 대해서 arr의 정보로 temp를 완성
        for a in range(N):
            temp += arr[a][lst[a]]
        # 최소 생산비용을 저장
        if ans > temp:
            ans = temp
        return
    # N개의 공장의 정보를 담고
    for i in range(N):
        # 이미 방문한 공장의 아니라면
        if i not in visited:
            # visited에 i 추가
            visited.append(i)
            # 현재까지의 합
            add += arr[n][i]
            # 다음 제품의 공장을 선택
            dfs(n+1, lst + [i])
            # n번째 값을 초기화
            visited.remove(i)
            # add 값 재설정
            add -= arr[n][i]

T = int(input())
for case in range(1, T+1):
    N = int(input())
    # 공장 정보를 담을 리스트 N*N 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]
    add = 0
    ans = 99 * N
    # 방문한 공장을 담을 리스트 visited
    visited = []
    # 0번부터, 공장 정보를 담을 리스트
    dfs(0,[])
    # 테스트케이스 번호와 최소생산비용을 출력
    print(f'#{case} {ans}')
