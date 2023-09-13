import sys
# NxN의 표의 길이인 홀수 N
N = int(sys.stdin.readline())
# 위치를 찾고자 하는 N^2이하의 자연수 하나 M
M = int(sys.stdin.readline())

numbers = [[0]*N for _ in range(N)]
direction = [(-1,0), (0, 1), (1, 0), (0, -1)]
direct = 0
cnt = 1
# M의 위치 mi, mj
mi, mj = N//2, N//2

# 현재 위치 ci, cj, numbers[ci][cj]에 시작 숫자 1을 저장
ci, cj = N//2, N//2
numbers[ci][cj] = 1

# for문
# for _ in range(N-1):
#     for _ in range(2):
#         di, dj = direction[direct]
#         for _ in range(cnt):
#             ni, nj = ci + di, cj + dj
#             numbers[ni][nj] = numbers[ci][cj] + 1
#             if numbers[ni][nj] == M:
#                 mi, mj = ni, nj
#             ci, cj = ni, nj
#         direct = (direct+1)%4
#     cnt += 1
# for _ in range(cnt-1):
#     di, dj = direction[direct]
#     ni, nj = ci + di, cj + dj
#     numbers[ni][nj] = numbers[ci][cj] + 1
#     if numbers[ni][nj] == M:
#         mi, mj = ni, nj
#     ci, cj = ni, nj

two = 1
# while문
while True:
    di, dj = direction[direct]
    break

for number in numbers:
    print(*number)
print(mi+1, mj+1)