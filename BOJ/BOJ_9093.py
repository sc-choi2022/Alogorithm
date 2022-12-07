import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    words = list(map(str, sys.stdin.readline().strip().split()))

    for word in words:
        print(word[::-1], end=' ')