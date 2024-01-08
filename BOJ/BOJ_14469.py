import sys

# 소의 마리수 N
N = int(sys.stdin.readline())
# 소의 정보를 저장하는 배열 cows
cows = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
cows.sort(key=lambda x:(x[0], x[1]))
# 모든 소가 농장에 입장하는 데 걸리는 최소 시간 answer
answer = -1

for cow in cows:
    # 소의 도착시간이 answer 이상인 경우
    if cow[0] >= answer:
        answer = sum(cow)
    # 이동시간을 추가가    else:
        answer += cow[1]
# answer 출력
print(answer)