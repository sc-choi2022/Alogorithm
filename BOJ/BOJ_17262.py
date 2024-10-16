import sys

# 욱제의 팬의 수 N
N = int(sys.stdin.readline())
# 팬이 머무는 시간 전체 범위의 기준 값 S, E
S, E = 0, 100001

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    S = max(S, s)
    E = min(E, e)

# 학교에 머물러야 하는 최소의 시간을 출력
if S-E < 0:
    print(0)
else:
    print(S-E)