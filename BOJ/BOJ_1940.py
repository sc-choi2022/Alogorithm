import sys

# 재료의 개수 N
N = int(sys.stdin.readline())
# 갑옷을 만드는데 필요한 수 M
M = int(sys.stdin.readline())
# 재료들의 고유 번호를 저장하는 배열 materials
materials = sorted(list(map(int, sys.stdin.readline().split())))
# 투 포인터를 활용할 start, end 값 초기화
start, end = 0, N-1
# 갑옷을 만들 수 있는 개수 answer
answer = 0

while start < end:
    add = materials[start] + materials[end]

    if add < M:
        start += 1
    elif add > M:
        end -= 1
    else:
        answer += 1
        start += 1
        end -= 1
# answer 출력
print(answer)