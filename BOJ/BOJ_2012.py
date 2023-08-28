import sys

# 학생들의 수 N
N = int(sys.stdin.readline())
# 예상등수 정보를 저장하는 배열 rank
rank = [int(sys.stdin.readline()) for _ in range(N)]
rank.sort()
# 불만도 bad
bad = 0
for i in range(1, N+1):
    bad += abs(i-rank[i-1])
# 불만도의 합을 최소로 할 때, 그 불만도를 출력
print(bad)