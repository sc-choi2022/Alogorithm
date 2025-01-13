import sys

# 횡단번호의 개수 N, 연속한 신호등의 개수 K, 고장난 신호등의 개수 B
N, K, B = map(int, sys.stdin.readline().split())
# 신호등의 상활을 저장하는 배열 light
light = [1] * N

for _ in range(B):
    # 고장난 신호등의 번호 number
    number = int(sys.stdin.readline())
    light[number-1] = 0

for i in range(1, N):
    light[i] += light[i-1]

# 연속 K개의 신호등이 존재하기 위해 필요한 최소 수리 개수 answer
answer = K-light[K-1]

for j in range(K, N):
    answer = min(answer, K-(light[j]-light[j-K]))

# answer 출력
print(answer)