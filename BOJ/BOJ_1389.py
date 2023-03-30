import sys

# 유저의 수 N, 친구 관계의 수 M
N, M = map(int, sys.stdin.readline().split())
INF = int(1e9)
# i와 j의 케인 베이컨의 단계를 저장할 배열 friend
friend = [[INF]*N for _ in range(N)]

for _ in range(M):
    # 친구관계인 a, b
    a, b = map(int, sys.stdin.readline().split())
    # friend배열에 a와 b의 친구단계정보를 저장
    friend[a-1][b-1] = 1
    friend[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            # 친구관계가 불가능한 경우
            if i == j:
                friend[i][j] = 0
            # 친구관계가 단계를 통해 가능한 경우
            else:
                friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])

# 케빈 베이컨의 수가 가장 작은 사람 answer, answer의 케빈 베이컨의 수 number
answer, number = 0, INF

for ii in range(N):
    if sum(friend[ii]) < number:
        answer = ii + 1
        number = sum(friend[ii])
# 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력
print(answer)