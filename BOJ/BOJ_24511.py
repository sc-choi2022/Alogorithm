import sys

# 자료구조의 개수 N
N = int(sys.stdin.readline())

# 수열 B의 각 위치의 자료구조를 저장하는 배열 A
A = list(map(int, sys.stdin.readline().split()))
# 수열 B
B = list(map(int, sys.stdin.readline().split()))
# 삽입할 수열의 길이 M
M = int(sys.stdin.readline())
# queuestack에 삽입할 원소를 담고 있는 수열 C
C = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(N):
    # queue인 경우
    if not A[i]:
        result.append(B[i])
result.reverse()
result = result + C

# 리턴값을 공백으로 구분하여 출력
print(*result[:M])