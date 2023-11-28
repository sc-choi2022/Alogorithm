import sys

# 접들의 개수 N
N = int(sys.stdin.readline())
# 점의 위치와 색상정보를 저장하는 배열 dots
dots = [(0, 0)] * N
# 화살표들의 길이의 합 answer
answer = 0

for i in range(N):
    dots[i] = tuple(map(int, sys.stdin.readline().split()))
dots.sort(key=lambda x:x[0])

for j in range(N):
    tmp = N
    for k in range(j-1, -1, -1):
        if dots[j][1] == dots[k][1]:
            tmp = dots[j][0] - dots[k][0]
            break

    for l in range(j+1, N):
        if dots[j][1] == dots[l][1]:
            tmp = min(tmp, dots[l][0]-dots[j][0])
            break
    answer += tmp
print(answer)