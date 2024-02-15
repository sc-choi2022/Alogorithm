import sys

# 월세를 내기 전 일수 N, 일할 수 있는 일수 M
N, M = map(int, sys.stdin.readline().split())
# 일급을 저장하는 배열 wages
wages = list(map(int, sys.stdin.readline().split()))

# 최대 이익 answer
answer = sum(wages[:M])

tmp = answer
for i in range(N-M):
    tmp -= wages[i]
    tmp += wages[M+i]
    answer = max(answer, tmp)
# 일을 해서 벌 수 있는 최대 이익을 출력
print(answer)