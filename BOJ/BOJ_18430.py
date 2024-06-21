import sys

def dfs(si, sj, power):
    global answer

    if sj == M:
        si, sj = si+1, 0

    if si == N:
        answer = max(answer, power)
        return

    if not visit[si][sj]:
        # 첫 번쨰 모양이 가능한 경우
        if si+1 < N and not visit[si+1][sj] and 0 <= sj-1 and not visit[si][sj-1]:
            visit[si][sj], visit[si+1][sj], visit[si][sj-1] = 1, 1, 1
            dfs(si, sj+1, power+2*wood[si][sj]+wood[si+1][sj]+wood[si][sj-1])
            visit[si][sj], visit[si+1][sj], visit[si][sj-1] = 0, 0, 0
        # 두 번째 모양이 가능한 경우
        if 0 <= si-1 and not visit[si-1][sj] and 0 <= sj-1 and not visit[si][sj-1]:
            visit[si][sj], visit[si-1][sj], visit[si][sj-1] = 1, 1, 1
            dfs(si, sj+1, power+2*wood[si][sj]+wood[si-1][sj]+wood[si][sj-1])
            visit[si][sj], visit[si-1][sj], visit[si][sj-1] = 0, 0, 0
        # 세 번째 모양이 가능한 겨우
        if 0 <= si-1 and not visit[si-1][sj] and sj+1 < M and not visit[si][sj+1]:
            visit[si][sj], visit[si-1][sj], visit[si][sj+1] = 1, 1, 1
            dfs(si, sj+1, power+2*wood[si][sj]+wood[si-1][sj]+wood[si][sj+1])
            visit[si][sj], visit[si-1][sj], visit[si][sj+1] = 0, 0, 0
        # 네 번쨰 모양이 가능한 경우
        if si+1 < N and not visit[si+1][sj] and sj+1 < M and not visit[si][sj+1]:
            visit[si][sj], visit[si+1][sj], visit[si][sj+1] = 1, 1, 1
            dfs(si, sj+1, power+2*wood[si][sj]+wood[si+1][sj]+wood[si][sj+1])
            visit[si][sj], visit[si+1][sj], visit[si][sj+1] = 0, 0, 0
    dfs(si, sj+1, power)

# 나무 재료의 세로 N, 가로 M
N, M = map(int, sys.stdin.readline().split())
# 나무 재료의 각 위치의 강도를 나타내는 배열 wood
wood = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 부메랑들의 강도의 합의 최댓값 answer
visit = [[0]*M for _ in range(N)]
answer = 0

dfs(0, 0, 0)

# 만들 수 있는 부메랑들의 강도 합의 최댓값을 출력
print(answer)