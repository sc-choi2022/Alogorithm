from collections import deque
import sys

# 판별해야하는 스트링 S
S = deque(sys.stdin.readline().rstrip())
answer = 'SUBMARINE'

# 첫 번째 경우를 체크하는 변수 flag, 0과 1 개수 확인하는 변수 cnt0, cnt1
flag, cnt0, cnt1 = False, 0, 0
while S and answer == 'SUBMARINE':
    if flag:
        if S[0] == '0':
            cnt0 += 1
            S.popleft()
        else:
            cnt1 += 1
            if cnt0 < 2:
                answer = 'NOISE'
                break
            if len(S) > 2 and S[1] == '0':
                # 첫 번째
                if S[2] == '0':
                    if cnt1 < 2:
                        answer = 'NOISE'
                        break
                    flag = False
                    cnt0, cnt1 = 0, 0
                    continue
                # 두 번째
                elif S[2] == '1':
                    flag = False
                    cnt0, cnt1 = 0, 0
            S.popleft()
    else:
        # 첫 번째
        if S[0] == '1':
            S.popleft()
            flag = True
        # 두 번째
        else:
            if len(S) >= 2:
                # 두 번째
                if S[1] == '1':
                    S.popleft()
                    S.popleft()
                # 00
                else:
                    answer = 'NOISE'
                    break
            else:
                answer = 'NOISE'
                break
if flag:
    # 첫 번째 패턴이 마무리 되지 않은 경우
    if cnt0 < 2 or cnt1 < 1:
        answer = 'NOISE'

# 잠수함의 엔진 소리에 해당하는 스트링이면 'SUBMARINE'을 출력
# 그렇지 않으면 'NOISE'를 출력
print(answer)