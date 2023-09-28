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
for _ in range(N-1):
    for _ in range(2):
        di, dj = direction[direct]
        for _ in range(cnt):
            ni, nj = ci + di, cj + dj
            numbers[ni][nj] = numbers[ci][cj] + 1
            if numbers[ni][nj] == M:
                mi, mj = ni, nj
            ci, cj = ni, nj
        direct = (direct+1)%4
    cnt += 1
for _ in range(cnt-1):
    di, dj = direction[direct]
    ni, nj = ci + di, cj + dj
    numbers[ni][nj] = numbers[ci][cj] + 1
    if numbers[ni][nj] == M:
        mi, mj = ni, nj
    ci, cj = ni, nj

# while문
number = 2
flag = False
while ci or cj:
    for _ in range(2):
        for _ in range(cnt):
            di, dj = direction[direct]
            ci += di
            cj += dj
            numbers[ci][cj] = number
            if number == M:
                mi, mj = ci, cj
            if ci == 0 and cj == 0:
                flag = True
                break
            number += 1
        if flag:
            break
        direct = (direct + 1)%4
    cnt += 1

# 표를 출력
for number in numbers:
    print(*number)
# 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력
print(mi+1, mj+1)