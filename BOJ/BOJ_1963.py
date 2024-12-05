from collections import deque
import sys

# 소수를 확인하는 함수 check
def check(number):
    for c in range(2, int(number**0.5)+1):
        if not number%c:
            return 0
    return 1

# 소수 여부를 저장하는 배열 prime
prime = [0] * 10000

for i in range(10000):
    prime[i] = check(i)

# 테스트케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 주어지는 두 소수 P1, P2
    P1, P2 = map(int, sys.stdin.readline().rstrip().split())
    # 변경한 비밀번호를 확인하는 배열 visit
    visit = [0] * 10000
    visit[P1] = 1
    P1, P2 = list(str(P1)), list(str(P2))
    queue = deque([(P1, 0)])

    while queue:
        # 비밀번호와 변경횟수 password, cnt
        password, cnt = queue.popleft()
        # 두 소수 사이의 변환에 필요한 최소 회수를 출력
        if password == P2:
            print(cnt)
            break

        for idx in range(4):
            for j in range(10):
                newP = password[::]
                newP[idx] = str(j)
                tmp = int(''.join(newP))
                # 변경가능한 비밀번호인 경우
                if 1000 <= tmp and not visit[tmp] and prime[tmp]:
                    visit[tmp] = 1
                    queue.append((newP, cnt+1))