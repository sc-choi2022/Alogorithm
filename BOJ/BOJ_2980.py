import sys

# 신호등의 개수 N, 도로의 길이 L
N, L = map(int, sys.stdin.readline().split())
# 도로의 끝까지 이동하는데 걸리는 시간 time
time = 0
# 신호등의 위치를 저장하는 배열 signal
signal = [0]*(L+1)
# 신호등의 정보를 저장하는 배열 info
info = [[] for _ in range(L+1)]

for _ in range(N):
    # 신호등의 위치 D, 빨간색이 지속되는 시간 R, 초록색이 지속되는 시간 G
    D, R, G = map(int, sys.stdin.readline().split())
    signal[D] = 1
    info[D] = [R, G]

# 상근이의 위치
idx = 0
while True:
    # 도로의 끝에 도달한 경우
    if idx == L:
        break
    # 신호등이 있는 위치인 경우
    if signal[idx]:
        tmpR, tmpD = info[idx]
        tmp = time%(tmpR+tmpD)
        if tmpR > tmp:
            time += tmpR-tmp
        else:
            idx += 1
            time += 1
    # 신호등이 없는 위치인 경우
    else:
        idx += 1
        time += 1
        
# 상근이가 도로의 끝까지 이동하는데 걸리는 시간을 출력
print(time)