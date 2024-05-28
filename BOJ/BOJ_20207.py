import sys

# 일정의 개수 N
N = int(sys.stdin.readline())
# 일자의 일정의 개수를 저장하는 배열 schedule
schedule = [0]*365
# 일정이 있는 기간의 시작 S, 끝 E
S, E = 365, 0

for _ in range(N):
    # 일정 하나의 시작 start, 끝 end
    start, end = map(int, sys.stdin.readline().split())
    # schedule에 일정 반영
    for i in range(start-1, end):
        schedule[i] += 1
    # 기간 갱신
    S, E = min(S, start-1), max(E, end)

# 코팅지의 면적 answer
answer = 0
# 코팅지의 높이 L1, 가로길이 L2
L1, L2 = 0, 0
for j in range(S, E):
    if schedule[j]:
        L2 += 1
        L1 = max(L1, schedule[j])
    else:
        answer += L1*L2
        L1, L2 = 0, 0
        
# 마지막 코팅지를 더한 코팅지의 면적 출력
print(answer+L1*L2)