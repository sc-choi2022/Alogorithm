import sys

# 사람의 수 N
N = int(sys.stdin.readline())

# 친구여부를 담는 배열 know
know = [list(sys.stdin.readline().strip()) for _ in range(N)]
# 2-친구 여부를 담을 배열 friend
friend = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            # 2-친구의 성립조건이 아니기 때문에 continue
            if i == k or j == k:
                continue
            # j와 k가 친구인 경우 혹은 i가 j와 k의 친구인 경우
            if know[j][k] == 'Y' or (know[j][i] == 'Y' and know[i][k] == 'Y'):
                # j와 k의 관계는 2-친구로 표시
                friend[j][k] = 1
# 가장 유명한 사람의 2-친구의 수 famous
famous = 0

# 가장 유명한 사람의 2-친구를 구하는 for문
for f in friend:
    famous = max(famous, sum(f))
# famous 출력
print(famous)