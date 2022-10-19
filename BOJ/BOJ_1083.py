import sys

# 배열A의 크기 N
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# 교환 횟수 S
S = int(sys.stdin.readline())

for i in range(N):
    # 현재 위치에서 변경가능한 범위안에서 max값을 찾아 max_num에 저장
    max_num = max(A[i: min(N, i + S + 1)])
    # max_num의 위치를 idx에 저장
    idx = A.index(max_num)

    # 최대값의 위치를 변경 i 위치까지 교환
    for j in range(idx, i, -1):
        A[j], A[j - 1] = A[j - 1], A[j]
    # 이동한 거리만큼 S값 감소
    S -= (idx - i)
    # 교환횟수를 충족한 경우 break
    if S == 0:
        break
# A를 출력
print(*A)