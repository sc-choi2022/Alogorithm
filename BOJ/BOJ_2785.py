import sys

# 체인의 개수 N
N = int(sys.stdin.readline())
# 각 체인의 길이를 저장하는 배열 chains
chains = sorted(list(map(int, sys.stdin.readline().split())))

# 필요한 고리의 최소 개수 answer
answer = 0
# 떨어진 체인의 개수 L
L = N
# 연결을 위해 사용하는 고리의 위치 idx, 해당 고리의 길이 use
idx = 0
use = chains[idx]

while L != 1:
    L -= 1
    # 고리를 사용하여 연결하는 경우
    if use > 0:
        use -= 1
        answer += 1
    # 고리를 모두 사용한 경우
    else:
        idx += 1
        use = chains[idx]

# 필요한 고리의 최소 개수를 출력
print(answer)