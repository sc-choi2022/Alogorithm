import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())
# 인덱스 N을 1, 2, 3으로 나타내는 수를 저장하는 배열 numbers
# 1로 만들 수 있는 방법 1로 값 초기화
numbers = [1]*10001

for i in range(2, 10001):
    numbers[i] += numbers[i-2]

for j in range(3, 10001):
    numbers[j] += numbers[j-3]

for _ in range(T):
    # 정수 N
    N = int(sys.stdin.readline())
    # N을 1, 2, 3의 합으로 나타내는 방법의 수를 출력
    print(numbers[N])