import sys

# 접들의 개수 N
N = int(sys.stdin.readline())
# 점의 색을 idx로 위치를 저장하는 배열 dots
dots = [[] for _ in range(N)]
# 화살표들의 길이 합 answer
answer = 0

for _ in range(N):
    # 위치 l, 색 c
    l, c = map(int, sys.stdin.readline().split())
    dots[c-1].append(l)

for dot in dots:
    if not dot:
        continue
    dot.sort()
    answer += dot[1]-dot[0] + dot[-1]-dot[-2]
    for i in range(1, len(dot)-1):
        answer += min(dot[i]-dot[i-1], dot[i+1]-dot[i])
# 표준 출력으로 모든 점에서 시작하는 화살표들의 길이 합을 출력
print(answer)