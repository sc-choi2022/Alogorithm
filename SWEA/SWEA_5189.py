import sys
sys.stdin = open('sample_input.txt')

def dfs(n, idx, temp):
    global ans
    # 모든 구역을 방문하기 전에 ans보다 temp의 값이 커지면 return
    if temp > ans:
        return
    # 모든 구역을 방문하면
    if n == N-1:
        # 돌아오는 값까지를 더한 결과와 ans중 작은 값을 ans에 저장
        ans = min(ans, temp + arr[idx][0])
        return
    # 1~N-1까지의 구역을 한번씩 방문하는 for문
    for i in range(1, N):
        if visited[i] == 0:
            # visited와 temp에 값을 1을 더하고 값을 추가한 후 dfs
            visited[i] = 1
            temp += arr[idx][i]
            dfs(n+1, i, temp)
            # dfs가 끝나고 visited와 temp값을 원래대로
            visited[i] = 0
            temp -= arr[idx][i]

T = int(input())
for case in range(1, T+1):
    # NxN 행렬의 N
    N = int(input())
    # NxN 행렬을 담을 리스트 arr
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문한 곳을 표시할 리스트 visited
    visited = [0]*N
    # 최소 배터리 사용량을 ans를 1000으로 초기화
    ans = 1000
    # 시작 위치, 이전 위치, 합을 모두 0으로 하여 dfs 실행
    dfs(0, 0, 0)
    # 테스트케이스번호와 ans출력
    print(f'#{case} {ans}')