import sys

# 플레이어의 수 N, 가진 카드 수 M
N, M = map(int, sys.stdin.readline().split())
cards = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
answer = [0] * N

for i in range(M):
    tmp = []
    for j in range(N):
        tmp.append(cards[j][i])
    M = max(tmp)
    for k in range(N):
        if M == tmp[k]:
            answer[k] += 1

winner = max(answer)

# 플레이어의 번호를 저장하는 배열
result = []
for l in range(N):
    if answer[l] == winner:
        result.append(l+1)
print(*result)