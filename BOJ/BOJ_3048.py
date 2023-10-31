import sys

# 첫번째 그룹의 개미의 수 N1, 두 번째 그룹의 개미의 수 N2
N1, N2 = map(int, sys.stdin.readline().split())
# 첫번째 그룹 A1, 두번째 그룹 A2
A1 = list(reversed(sys.stdin.readline().rstrip()))
A2 = list(sys.stdin.readline().rstrip())
A = A1 + A2

group = dict()
for a1 in A1:
    group[a1] = 0
for a2 in A2:
    group[a2] = 1

# 개미의 이동 시간 T초
T = int(sys.stdin.readline())
for _ in range(T):
    for i in range(N1+N2-1):
        # 그룹 A1와 그룹 A2가 만난 경우
        if group[A[i]] == 0 and group[A[i+1]] == 1:
            A[i], A[i+1] = A[i+1], A[i]
            # 선두 개미가 위치를 변경한 경우 break
            if A[i+1] == A1[-1]:
                break
# T초가 지난 후에 개미의 순서를 출력
print(''.join(A))