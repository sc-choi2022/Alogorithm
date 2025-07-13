import sys

# 점의 개수 N
N = int(sys.stdin.readline())

# 점의 정보를 저장하는 배열 dots
dots = [map(int, sys.stdin.readline().split()) for _ in range(N)]
dots.sort()

result = 0

for i in range(N):
    if i == 0:
        if dots[i][0] == dots[i+1][0]:
            result += result[i+1][1] - result[i][1]
    elif i == N-1:
        if dots[i][0] == dots[i-1][0]:
            result += result[i][1] - result[i-1][1]
    else:
        if dots[i][0] == dots[i+1][0] and dots[i][0] == dots[i-1][0]:
            if (dots[i+1][1]-dots[i][1] > dots[i][1]-dots[i-1][1]):
                result += dots[i][1] - result[i-1][1]
            else:
                result += dots[i+1][1] - result[i][1]
        elif dots[i][0] == dots[i+1][0]:
            result += dots[i+1][1] - dots[i][1]
        elif dots[i][0] == dots[i-1][0]:
            result += dots[i][1] - dots[i-1][1]
        else:
            result += 0

print(result)