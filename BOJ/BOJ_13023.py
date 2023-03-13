import sys

def dfs(num, depth):
    global answer

    visit[num] = 1
    if depth == 5:
        answer = 1
        return

    for f in friend[num]:
        if visit[f] == 0:
            dfs(f, depth + 1)
            visit[f] = 0

# 사람의 수 N, 친구 관계의 수 M
N, M = map(int, sys.stdin.readline().split())
# 친구의 정보를 담을 배열 friend
friend = [[] for _ in range(N)]
# 친구로 확인했는지 여부를 저장할 visit
visit = [0] * N
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(N):
    dfs(i, 1)
    visit[i] = 0
    # 조건의 친구관계가 존재한다면 break
    if answer:
        break
# 문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력
print(answer)