import sys

# 막대기의 개수 N
N = int(sys.stdin.readline())
# 막대기의 정보를 담을 리스트 bars
bars = [0] * N
# 현재 높이 h
h = 0
# 출력할 보이는 막대기의 개수 ans 0으로 초기화
ans = 0

for i in range(N):
    bars[i] = int(sys.stdin.readline())

# 오른쪽 막대기부터 보이는 높이를 확인 후 ans에 반영
for j in range(N - 1, -1, -1):
    if bars[j] > h:
        h = bars[j]
        ans += 1
# 보이는 막대기의 개수를 출력
print(ans)