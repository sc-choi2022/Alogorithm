import sys

# 국가의 수 N, 등수를 알고 싶은 국가 K
N, K = map(int, sys.stdin.readline().split())
olympic = [list(map(int, input().split())) for _ in range(N)]
olympic.sort(key=lambda x:(-x[1], -x[2], -x[3]))
# K의 등수
idx = [olympic[i][0] for i in range(N)].index(K)
# K와 동일한 메달 수를 가지고 있는 경우를 확인
for j in range(N):
    if olympic[idx][1:] == olympic[j][1:]:
        print(j+1)
        break