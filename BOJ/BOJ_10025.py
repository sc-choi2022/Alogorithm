import sys

# 얼음 양동이의 개수 N, 좌우 가능 거리 K
N, K = map(int, sys.stdin.readline().split())
# 얼음 양과 위치를 저장하는 배열 ice
ice = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
ice.sort(key=lambda x:x[1])
# 구간의 기준이 되는 양동이의 위치 left, right
left, right = 0, 0
# 최적 위치로부터의 얼음들의 최대 합 answer
answer = 0
# 누적합을 저장하는 변수 tmp
tmp = ice[left][0]

while right < N:
    # 범위가 K보다 더 먼 경우
    if ice[right][1] - ice[left][1] > 2*K:
        tmp -= ice[left][0]
        left += 1
    else:
        answer = max(answer, tmp)
        right += 1
        if right < N:
            tmp += ice[right][0]

# 최적 위치로부터 K만큼 떨어진 거리 내에 있는 얼음들의 합(최댓값)을 출력
print(answer)