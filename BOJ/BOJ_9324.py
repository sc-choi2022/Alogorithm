from collections import defaultdict
import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 메세지 M
    M = sys.stdin.readline().rstrip()
    # 메세지의 알파벳 개수를 저장하는 딕셔너리 alphabet
    alphabet = defaultdict(int)
    # 메세지의 길이 L
    L = len(M)
    # 문자가 세 번째 등장 여부를 저장하는 변수 flag
    flag = False

    for i in range(L):
        # i번째가 반복되어야하는 문자인 경우
        if flag:
            flag = False
            continue
        # alphabet에 갯수 반영
        alphabet[M[i]] += 1
        # M[i]이 3번 등장한 경우
        if alphabet[M[i]] == 3:
            # 정확한 변형인 경우
            if i+1 < L and M[i+1] == M[i]:
                alphabet[M[i]] = 0
                flag = True
            # 정확하지 않은 변형인 경우 FAKE 출력
            else:
                print('FAKE')
                break
    # 메세지가 진짜인 경우 OK 출력
    else:
        print('OK')