import sys

def check(line):
    slope = [0] * N
    for i in range(N-1):
        # 길의 높이가 동일한 경우
        if line[i] == line[i+1]:
            continue
        # 경사로를 놓을 수 없는 경우
        elif abs(line[i] - line[i+1]) > 1:
            return False
        # 내리막 경사가 필요한 경우
        elif line[i] > line[i+1]:
            # 낮은 칸의 높이 tmp
            tmp = line[i+1]
            if i + L >= N:
                return False
            else:
                for j in range(i+1, i+L+1):
                    # 높이가 다른 경우 혹은 경사로가 이미 존재하는 경우
                    if tmp != line[j] or slope[j]:
                        return False
                    slope[j] = 1
        # 오르막 경사가 필요한 경우
        else:
            tmp = line[i]
            if i-L+1 < 0:
                return False
            else:
                for j in range(i, i-L, -1):
                    if tmp != line[j] or slope[j]:
                        return False
                    slope[j] = 1
    # 지나갈 수 있는 경우 True를 return
    return True

# 지도의 크기 N, 경사로의 길이 L
N, L = map(int, sys.stdin.readline().split())
# 가로방향을 확인하는 zido, 세로방향을 확인하는 zidoT
zido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
zidoT = list(map(list, zip(*zido)))

# 길의 개수 answer
answer = 0

for z in range(N):
    if check(zido[z]):
        answer += 1
    if check(zidoT[z]):
        answer += 1
# 지나갈 수 있는 길의 개수 출력
print(answer)