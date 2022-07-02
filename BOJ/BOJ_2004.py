import sys

# N!에서 twofive의 개수를 찾아 출력하는 함수 countNumber
def countNumber(N, twofive):
    # return할 개수 cnt
    cnt = 0
    # 5의 개수를 cnt해서 cnt에 N을 추가
    while N:
        N //= twofive
        cnt += N
    # cnt return
    return cnt

# 정수 N, M
N, M = map(int, sys.stdin.readline().split())
# 조합 조건에 맞에 countNumber함수를 확인하여 출력
print(min(countNumber(N, 5) - countNumber(N-M, 5) - countNumber(M, 5), countNumber(N, 2) - countNumber(N-M, 2) - countNumber(M, 2)))