import sys

# 주어지는 N, M
N, M = map(int, sys.stdin.readline().split())

# N을 N번한 값을 ans에 저장
ans = str(N) * N
# ans의 앞 M자리 출력
print(ans[:M])

