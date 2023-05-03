import sys

# 트럭의 개수 N, 다리의 길이 W, 다리의 최대하중 L
N, W, L = map(int, sys.stdin.readline().split())

# 트럭의 무게를 담은 배열 truck
truck = list(map(int, sys.stdin.readline().split()))
# idx시간에 트럭의 무게를 저장하는 배열 time
time = [0] * 100001
# 트럭의 시작시간 idx을 1로 초기화
idx = 1
for i in range(N):
    # 현재 트럭의 무게 now
    now = truck[i]
    # 트럭이 다리에 올라가는 시간을 구하는 while문
    while True:
        if time[idx] + now > L:
            idx += 1
        else:
            break
    # 현재 트럭이 다리위에 있는 시간동안 무게를 time에 반영
    for j in range(W):
        time[idx+j] += now
    # 다음 트럭은 적어도 시간 1 이후에 가능하다.
    idx += 1
# 모든 트럭들이 다리를 건너는 최단시간을 출력
print(idx + W - 1)