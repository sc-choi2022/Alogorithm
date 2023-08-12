import sys, math

# 테스트 케이스들의 수 C
C = int(sys.stdin.readline())
# 채점 시스템이 1초에 가능한 동작의 개수 action
action = 100000000

for _ in range(C):
    # 시간 복잡도 S, 입력의 최대 범위 N, 테스트 케이스의 수 T, 제한시간 L
    S, N, T, L = sys.stdin.readline().rstrip().split()
    cnt = 0
    if S[-2] == 'N':
        # O(N)
        if len(S) == 4:
            cnt = int(N) * int(T)
        # O(2^N)
        else:
            cnt = 2**int(N)*int(T)
    # O(N^2)
    elif S[-2] == '2':
        cnt = int(N)**2 * int(T)
    # O(N^3)
    elif S[-2] == '3':
        cnt = int(N)**3 * int(T)
    # O(N!)
    else:
        cnt = math.factorial(int(N)) * int(T)

    # 시간 초과가 나지 않으면 "May Pass."
    if action * int(L) >= cnt:
        print('May Pass.')
    # 시간 초과가 나면 "TLE!"
    else:
        print('TLE!')