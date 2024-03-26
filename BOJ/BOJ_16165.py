import sys

# 걸그룹의 수 N, 퀴즈의 개수
N, M = map(int, sys.stdin.readline().split())
girlgroup = dict()

for _ in range(N):
    group = sys.stdin.readline().rstrip()
    number = int(sys.stdin.readline())
    lst = [sys.stdin.readline().rstrip() for _ in range(number)]
    lst.sort()
    girlgroup[group] = lst

for _ in range(M):
    # 퀴즈 이름
    Q = sys.stdin.readline().rstrip()
    # 퀴즈의 종류
    T = int(sys.stdin.readline())

    # 멤버의 속한 팀의 이름인 경우
    if T:
        for key, value in girlgroup.items():
            if Q in value:
                print(key)
                break
    # 해당 팀에 속한 멤버의 이름을 사전순으로 한 명씩 출력
    else:
        members = girlgroup[Q]
        for member in members:
            print(member)