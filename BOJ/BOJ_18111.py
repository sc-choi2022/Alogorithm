import sys

# 집터의 크기 N, M, 블록의 개수 B
N, M, B = map(int, sys.stdin.readline().split())
# 땅의 높이를 저장하는 배열 ground
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 최소시간 time, 최대 높이 height
time, height = int(1e9), 0

for block in range(257):
    # 올려두는 블록 수 put, 제거하는 블록 수 take
    put, take = 0, 0

    for i in range(N):
        for j in range(M):
            g = ground[i][j]
            if g > block:
                take += g - block
            else:
                put += block - g
    # 사용 블록수가 가진 블록수보다 많은 경우
    if put > take + B:
        continue
    # take와 put에 따른 소요시간 tmp
    tmp = 2 * take + put

    if time >= tmp:
        time = tmp
        height = block
# 땅을 고르는 데 걸리는 최소 시간과 최대 땅의 높이를 출력
print(time, height)

# 방법2
import sys

# 집터의 크기 N, M, 블록의 개수 B
N, M, B = map(int, sys.stdin.readline().split())
# idx높이의 집터의 개수를 저장하는 배열 block
block = [0] * 257
for _ in range(N):
    # idx높이의 집터의 개수를 저장하는 방법
    for i in map(int, sys.stdin.readline().split()):
        block[i] += 1
# 쌓여있는 블록의 개수 have
have = sum(j*block[j] for j in range(257))
# 높이가 0일 때 소요되는 시간과 높이 0을 저장한 튜플 answer
answer = (2*have, 0)
# 높이가 0일 때 필요한 블록수 need
need = 0
# 현재 높이의 블록와 같거나 작은 높이의 집터의 개수 cnt를 block[0]으로 초기화
cnt = block[0]
# 한 층에 필요한 블록의 개수
NM = N * M

for ii in range(1, 257):
    # ii높이가 되기 위해 필요한 블록수 갱신
    need += cnt
    # 이전 높이에서 ii높이가 되면서 사용된 블록 수
    have -= NM - cnt
    # ii높이 이하의 블록수를 갱신
    cnt += block[ii]

    # 보유한 블록 수보다 필요한 블록이 많은 경우 break
    if have + B < need:
        break
    else:
        # answer의 소요시간과 높이를 갱신
        # min을 활용하기 위해 높이를 음수값으로 저장
        answer = min(answer, (have*2+need, -ii))
# 땅을 고르는 데 걸리는 최소 시간과 최대 땅의 높이를 출력
print(answer[0], -answer[1])