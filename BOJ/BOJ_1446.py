import sys

# 지름길의 개수 N과 고속도로의 길이 D
N, D = map(int, sys.stdin.readline().split())
# 지름길의 정보를 저장하는 배열 shortcuts
shortcuts = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
shortcuts.sort(key=lambda x:(x[0], x[1], x[2]))
# i 위치까지 가는데 걸리는 최단거리를 저장하는 배열 dp
dp = [i for i in range(D+1)]

for j in range(D+1):
    # j번째 위치까지의 길이를 최솟값으로 갱신
    dp[j] = min(dp[j], dp[j-1]+1)

    # 지름길이 존재하는 경우
    while shortcuts:
        # j 위치가 가장 근처의 지름길의 위치가 아닌 경우 break
        if shortcuts[0][0] > j:
            break
        # 지름길의 시작위치 S, 도착위치 E, 지름길의 길이 L
        S, E, L = shortcuts.pop(0)
        # 지름길을 통해 목표 길이내에 거리 갱신이 가능한 경우
        if S == j and E <= D and dp[j] + L < dp[E]:
            dp[E] = dp[j] + L
# 운전해야하는 최솟값을 출력
print(dp[D])