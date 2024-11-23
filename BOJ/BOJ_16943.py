import sys

def number(idx, num):
    global C

    if idx == N and int(num) < B:
        C = max(C, int(num))
        return
    for i in range(N):
        if idx == 0 and A[i] == '0':
            continue
        if not visit[i]:
            visit[i] = 1
            number(idx+1, num+A[i])
            visit[i] = 0

# 정답 C의 기준 값 A, B
A, B = sys.stdin.readline().rstrip().split()

# 조건에 부합하는 C가 없는 경우
if len(A) > len(B):
    print(-1)
else:
    A, B = sorted(list(A), reverse=True), int(B)
    # 배열 A의 길이 N
    N = len(A)
    # 사용한 숫자를 확인하는 배열 visit
    visit = [0] * N
    # 구하는 정수 C
    C = -1
    number(0, '')
    # C를 출력
    print(C)