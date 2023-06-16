from itertools import combinations
import sys

# 볼록 다각형 점 수 N
N = int(sys.stdin.readline())
# 다각형의 점을 저장하는 배열 dots
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 가능한 넓이의 최댓값 answer
answer = 0
# dots의 세개의 점의 모든 경우의 수를 저장하는 배열 combi
combi = list(combinations(dots, 3))

for c in combi:
    # 벡터의 외적을 활용하여 삼각형의 넓이 구하기
    area = abs((c[1][0]-c[0][0])*(c[2][1]-c[0][1])-(c[2][0]-c[0][0])*(c[1][1]-c[0][1]))/2
    answer = max(answer, area)
# answer 출력
print(answer)