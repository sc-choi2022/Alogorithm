import sys
from collections import deque
# 테스트 케이스 T
T = int(sys.stdin.readline())

# 필요한 최소한의 명령어를 담을 변수 ans
ans = ''
for _ in range(T):
    # 변환할 정수 A, 변환하여 만들 정수 B
    A, B = map(int, sys.stdin.readline().split())

    queue = deque()
    # 명령어를 입력하지 않는 상태의 A와 명령어를 queue에 추가
    queue.append((A, ''))
    # B의 범위에서 만들어진 숫자 여부를 표시할 visited
    visited = [0]*10000
    while queue:
        # 숫자 number, 명령어 word
        number, word = queue.popleft()
        # number가 B를 만들었다면 ans에 word를 할당하고 break
        if number == B:
            ans = word
            break
        # 명령어 D
        numD = (2*number)%10000
        if visited[numD] == 0:
            queue.append((numD, word + 'D'))
            visited[numD] = 1
        # 명령어 S
        numS = (number-1)%10000
        if visited[numS] == 0:
            queue.append((numS, word + 'S'))
            visited[numD] = 1
        # 명령어 L
        numL = (number*10 + number//1000)%10000
        if visited[numL] == 0:
            queue.append((numL, word + 'L'))
            visited[numL] = 1
        # 명령어 R
        numR = (number%10*1000+number//10)%10000
        if visited[numR] == 0:
            queue.append((numR, word + 'R'))
            visited[numR] = 1
    # 최소한의 명령어 출력
    print(ans)