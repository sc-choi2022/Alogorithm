import sys

# 여학색의 수 N, 남학생의 수 M, 인턴쉽에 참여해야하는 인원 K
N, M, K = map(int, sys.stdin.readline().split())
# 만들 수 있는 팀의 최대 수
team = min(N//2, M)
# team에 속하지 못하는 학생의 수 student
student = N + M - 3*team

while student < K:
    team -= 1
    student += 3
# 만들 수 있는 팀의 최대 개수을 출력
print(team)