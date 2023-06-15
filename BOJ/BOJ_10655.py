import sys

# 체크포인트의 수 N
N = int(sys.stdin.readline())
# 체크포인트를 담을 배열 checkpoint
checkpoint = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 체크포인트 사이의 거리를 담을 배열 distance
distance = [0] * N
# 최소 거리 answer
answer = 0

for i in range(1, N):
    distance[i] = abs(checkpoint[i-1][0] - checkpoint[i][0]) + abs(checkpoint[i-1][1] - checkpoint[i][1])
answer = sum(distance)
# 모든 거리 사이의 합 all
all = sum(distance)

for j in range(1, N-1):
    # 새로 구해지는 거리 tmp
    tmp = abs(checkpoint[j-1][0] - checkpoint[j+1][0]) + abs(checkpoint[j-1][1] - checkpoint[j+1][1])
    # tmp를 반영한 거리와 기존 거리 중 작은 값을 answer에 저장
    answer = min(answer, all+tmp-distance[j]-distance[j+1])
# answer 출력
print(answer)