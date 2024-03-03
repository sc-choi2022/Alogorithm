import sys

# 개강총회를 시작한 시간 S, 개강총회를 끝낸 시간 E, 개강총회 스트리밍을 끝낸 시간 Q
S, E, Q = sys.stdin.readline().rstrip().split()
S1, S2 = map(int, S.split(':'))
E1, E2 = map(int, E.split(':'))
Q1, Q2 = map(int, Q.split(':'))

# 입장 확인한 인원을 저장하는 set enter
enter = set()

while True:
    try:
        time, nickname = sys.stdin.readline().rstrip().split()
        T1, T2 = map(int, time.split(':'))
        continue
    except:
        break

# print(cnt)