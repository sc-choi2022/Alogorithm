import sys

# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 D, 연속해서 먹는 접시의 수 K, 쿠폰 번호 C
N, D, K, C = map(int, sys.stdin.readline().split())
# 벨트에 올려져 있는 회전 초밥의 정보를 저장하는 배열 sushi
sushi = [int(sys.stdin.readline()) for _ in range(N)]

# 손님이 먹을 수 있는 초밥 가짓수의 최댓값 answer
answer = 0