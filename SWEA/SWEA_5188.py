import sys
sys.stdin = open('sample_input.txt')

def dfs(si, sj, temp):
    global ans
    # 도착이전에 ans값을 temp가 넘는다면 return
    if temp > ans:
        return
    # 목적지에 도착
    if (si, sj) == (N-1, N-1):
        # temp와 ans를 비교하여 작은 값을 ans에 저장
        if ans > temp:
            ans = temp
        return
    # 두개의 방향에 대해 다음 위치를 설정
    for di, dj in ((0,1), (1,0)):
        ni = si + di
        nj = sj + dj
        # 다음 위치가 범위 안에 있다면
        if 0 <= ni < N and 0 <= nj < N:
            # temp에 값을 추가 후 다음 위치의 dfs 실행
            temp += arr[ni][nj]
            dfs(ni, nj, temp)
            # temp값을 되돌린다.
            temp -= arr[ni][nj]

T = int(input())
for case in range(1, T + 1):
    # N*N 행렬의 N
    N = int(input())
    # N*N 행렬을 담을 리스트 arr
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최대값 130으로 ans값 초기화
    ans = 130
    # 시작 위치, 0,0과 (0,0)의 값 arr[0][0]으로 dfs 시작
    dfs(0, 0, arr[0][0])
    # 테스트 케이스 번호와 ans 출력
    print(f'#{case} {ans}')