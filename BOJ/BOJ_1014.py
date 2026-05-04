import sys

# 테스트 케이스 C
C = int(input())

for _ in range(C):
    # N행 M열의 N, M
    N, M = map(int, sys.stdin.readline().split())
    # 자리를 저장하는 배열 seat
    seat = [list(sys.stdin.readline()) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]