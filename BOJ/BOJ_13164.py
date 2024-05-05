import sys

# 원생의 수 N, 조의 개수 K
N, K = map(int, sys.stdin.readline().split())
# 원생의 키를 저장하는 배열 heights
heights = list(map(int, sys.stdin.readline().split()))
# 서로 인접한 원생들 키의 차이를 저장하는 배열 difference
difference = [0] * (N-1)

for i in range(N-1):
    difference[i] = heights[i+1] - heights[i]
difference.sort(reverse=True)

# 티셔츠 만드는 비용이 최소가 되도록 K개의 조로 나누었을 때, 티셔츠 만드는 비용을 출력
print(sum(difference[K-1:]))