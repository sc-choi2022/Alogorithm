import math, sys

# 가로수의 수 N
N = int(sys.stdin.readline())
# 가로수의 위치를 저장하는 배열 trees
trees = [int(sys.stdin.readline()) for _ in range(N)]
# 가로수 사이의 거리를 저장하는 배열 gap
gap = [0] * (N-1)
for i in range(N-1):
    gap[i] = trees[i+1]-trees[i]
# 가로수 사이의 거리의 최대공약수 number
number = math.gcd(*gap)
# 심어야하는 가로수의 개수를 저장하는 answer
answer = 0

for j in range(N-1):
    answer += gap[j]//number - 1
# 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수 출력
print(answer)