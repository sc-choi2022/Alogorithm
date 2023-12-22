import sys

def dfs(number):
    visit = [0]*(N+1)
    visit[number] = 1
    stack = [number]

    while stack:
        current = stack.pop()
        if not visit[graph[current]]:
            visit[graph[current]] = 1
            stack.append(graph[current])

    return sum(visit)

# 선배의 명수 N
N = int(sys.stdin.readline())
# 선배들의 연결정보를 저장하는 배열 graph
graph = [0] + [int(sys.stdin.readline()) for _ in range(N)]
# 현재까지 가장 많은 만나는 수 num, 선배의 번호 answer
num, answer = 0, 0

for j in range(1, N+1):
    tmp = dfs(j)

    if tmp > num:
        num = tmp
        answer = j
# answer 출력
print(answer)