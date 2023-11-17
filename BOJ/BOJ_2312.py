from collections import defaultdict
import sys

# 테스트 케이스 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 양의 정수 N
    N = int(sys.stdin.readline())
    answer = defaultdict(int)
    i = 2

    while True:
        if N == 1:
            break
        if N%i:
            i += 1
        else:
            N //= i
            answer[i] += 1
    for key, value in answer.items():
        print(key, value)