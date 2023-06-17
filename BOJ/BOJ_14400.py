import sys

# 주요 고객들의 수 N
N = int(sys.stdin.readline())
# 고객들의 x좌표와 y좌표를 저장하는 배열 lst_x, lst_y
lst_x, lst_y = [0]*N, [0]*N

for i in range(N):
    lst_x[i], lst_y[i] = map(int, sys.stdin.readline().split())
lst_x.sort()
lst_y.sort()

# 편의 점의 위치 x, y
x, y = lst_x[N//2], lst_y[N//2]

# 최소 거리 합 answer
answer = 0
for j in range(N):
    answer += abs(lst_x[j]-x) + abs(lst_y[j]-y)
# answer 출력
print(answer)