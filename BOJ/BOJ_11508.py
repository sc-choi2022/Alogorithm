import sys

# 유제품의 수 N
N = int(sys.stdin.readline())
# 유제품의 가격을 저장하는 배열 C
C = [int(sys.stdin.readline()) for _ in range(N)]
C.sort(reverse=True)
# 유제품을 모두 살 때 필요한 최소비용 answer
answer = sum(C)

for i in range(2, N, 3):
    answer -= C[i]
# N개의 유제품을 모두 살 때 필요한 최소비용을 출력
print(answer)