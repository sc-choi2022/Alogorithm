import sys

# 개강총회를 시작한 시간 S, 개강총회를 끝낸 시간 E, 개강총회 스트리밍을 끝낸 시간 Q
S, E, Q = sys.stdin.readline().rstrip().split()
S1, S2 = map(int, S.split(':'))
E1, E2 = map(int, E.split(':'))
Q1, Q2 = map(int, Q.split(':'))

# 입장 확인한 인원을 저장하는 set enter
enter = set()
# 출석이 확인된 학회원의 인원 수 answer
answer = 0

while True:
    try:
        time, nickname = sys.stdin.readline().rstrip().split()
        T1, T2 = map(int, time.split(':'))
        # 입장 확인
        if T1 < S1 or (S1 == T1 and S2 >= T2):
            enter.add(nickname)
        # 퇴장 확인
        # 총회가 끝난 후 채팅 & 스트리밍이 끝나기 전에 채팅
        elif ((T1 > E1) or (T1 == E1 and T2 >= E2)) and ((T1 < Q1) or (T1 == Q1 and T2 <= Q2)):
            if nickname in enter:
                enter.remove(nickname)
                answer += 1
    except:
        break
# 출석이 확인된 학회원의 인원 수를 출력
print(answer)