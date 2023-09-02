import sys

# 곡의 개수 N, 시작 볼륨 S, 기준 값 M
N, S, M = map(int, sys.stdin.readline().split())
# 볼륨의 정보를 저장하는 volumes
volumes = list(map(int, sys.stdin.readline().split()))

dp = [[0*(M+1)] for _ in range(N+1)]