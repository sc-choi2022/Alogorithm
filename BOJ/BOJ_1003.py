import sys

def fibonacci(N):
    # 0이 출력되는 횟수 리스트 zeros
    # 1이 출력되는 횟수 리스트 ones
    # 리스트에 3부터 리스트를 추가
    if N >= 3:
        for i in range(len(zeros)-1, N):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    print(zeros[N], ones[N])

zeros = [1, 0, 1]
ones = [0, 1, 1]
# 테스트 케이스 수
T = int(sys.stdin.readline())
for _ in range(T):
    # 자연수 N
    N = int(sys.stdin.readline())
    # N에 대한 0과 1의 출력횟수를 출력하는 함수 fibonacci
    fibonacci(N)