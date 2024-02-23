import sys

# 테스트케이스 수 T
T = int(sys.stdin.readline())

# 피보나치 수를 저장하는 배열 fibonacci
fibonacci = [0, 1] + [0] * 44

for f in range(2, 45+1):
    fibonacci[f] = fibonacci[f-2] + fibonacci[f-1]

for _ in range(T):
    # 정수 N
    N = int(sys.stdin.readline())
    # 합이 N이 되는 피보나치 수를 저장하는 배열 answer
    answer = []

    for i in range(45, 0, -1):
        if fibonacci[i] <= N:
            answer.append(fibonacci[i])
            N -= fibonacci[i]

            if N == 0:
                # 피보나치 수들의 합이 주어진 정수에 대해 같게 되는 최소수의 피보나치 수들을 증가하는 순서로 출력
                answer.sort()
                print(*answer)
                break