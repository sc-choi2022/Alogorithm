import sys

# 정수의 개수 N
N = int(sys.stdin.readline())
# 정수를 저장하는 배열 number
number = list(map(int, sys.stdin.readline().split()))

minN = number[0]
# 조건의 최댓값을 저장하는 배열 answer
answer = [0] * N

for i in range(1, N):
    minN = min(minN, number[i])
    answer[i] = max(answer[i-1], number[i]-minN)

# answer을 출력
print(*answer)