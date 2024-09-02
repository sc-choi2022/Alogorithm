import sys

# 현재의 피로도 P, 장신구의 개수 N
P, N = map(int, sys.stdin.readline().split())
# 장신구 제작 시 피로도를 저장하는 배열 A
A = sorted(list(map(int, sys.stdin.readline().split())))
# 장신구의 최대 개수 cnt
cnt = 0

while A and P < 200:
    fatigue = A.pop(0)
    cnt += 1
    P += fatigue
# 제작할 수 있는 장신구의 최대 개수를 출력
print(cnt)