import sys

# 수열 A의 길이 N, 질문의 개수 Q
N, Q = map(int, sys.stdin.readline().split())
# 수열 A을 비내림차순으로 정렬
A = list(sorted(map(int, sys.stdin.readline().split())))
# 누적합을 저장하는 배열 B
B = [0] + A[::]

for i in range(2, N+1):
    B[i] += B[i-1]

for _ in range(Q):
    # 질문을 의미한 수 L, R
    L, R = map(int, sys.stdin.readline().split())
    # 답을 출력
    print(B[R]-B[L-1])