# 정수 N, M
N, M = map(int, input().split())
# 최소 쪼개기 개수 출력
print((N-1)+N*(M-1))