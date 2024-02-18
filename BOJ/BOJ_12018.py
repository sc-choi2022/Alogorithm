import sys

# 과목 수 N, 주어진 마일리지 M
N, M = map(int, sys.stdin.readline().split())
# 과목을 듣기 위해 필요한 최소 마일리지를 저장하는 배열 limit
limit = [0]*N
# 최대로 들을 수 있는 과목의 개수 answer
answer = 0

for i in range(N):
    # 과목에 신청한 사람의 수 P, 수강인원 L
    P, L = map(int, sys.stdin.readline().split())
    # 과목에 신청한 마일리지를 저장하는 배열 mileage
    mileage = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    # 신청한 사람의 수가 수강인원 이상인 경우
    if P >= L:
        limit[i] = mileage[L-1]
    # 신청한 사람의 수가 수강인원 이하인 경우
    else:
        limit[i] = 1
# 필요한 최소 마일리지를 정렬
limit.sort()
# 수강을 위한 사용한 마일리지를 저장하는 병수 use
use = 0
for j in range(N):
    # j번째 강의를 수강할 수 있는 경우
    if use + limit[j] <= M:
        use += limit[j]
        answer += 1
    # 더이상 강의를 수강할 수 없는 경우
    else:
        break

# 주어진 마일리지로 최대로 들을 수 있는 과목 개수를 출력
print(answer)