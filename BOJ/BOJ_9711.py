import sys

# 피보나치수를 저장하는 배열 fibonacci
fibonacci = [0]*10001
fibonacci[1], fibonacci[2] = 1, 1

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())
idx = 2
for i in range(1, T+1):
    P, Q = map(int, sys.stdin.readline().split())

    if not fibonacci[P]:
        for j in range(idx, P+1):
            fibonacci[j] = fibonacci[j-2]+fibonacci[j-1]
        idx = P
    # 각 테스트 케이스마다 "Case #x: M" 형식으로 출력
    print(f'Case #{i}: {fibonacci[P] % Q}')
