import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

numbers = [1]*10001

for i in range(2, 10001):
    numbers[i] += numbers[i-2]
print()
print(numbers[:20])
for j in range(3, 10001):
    numbers[j] += numbers[j-3]
print(numbers[:20])
for _ in range(T):
    # 정수 N
    N = int(sys.stdin.readline())
    # N을 1, 2, 3의 합으로 나타내는 방법의 수를 출력
    print(numbers[N])
print(numbers[:20])