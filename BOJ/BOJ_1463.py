import sys
# dfs을 활용하여 모든 경우의 수를 확인
def dfs(N, cnt):
    global ans
    # 1에 도달했다면 ans와 비교하여 ans을 재할당
    if N == 1:
        ans = min(cnt, ans)
        return
    # 이미 ans의 횟수에 도달하면 백트래킹
    if cnt >= ans:
        return
    # 3으로 나누어지는 경우
    if N % 3 == 0:
        dfs(N//3, cnt + 1)
    # 2로 나누어지는 경우
    if N % 2 == 0:
        dfs(N//2, cnt + 1)
    # 1을 빼는 경우
    dfs(N-1, cnt + 1)
# 정수 N
N = int(sys.stdin.readline())
# ans의 값을 1000000으로 초기화
ans = 1000000
# N와 0회를 시작으로 dfs 실행
dfs(N, 0)
# ans을 출력
print(ans)