import sys

# 변 AB와 변 AC의 길이 N, 점의 개수 K
N, K = map(int, sys.stdin.readline().split())
# 문제에서 요구하는 정답을 x라고 할 때, x보다 크지 않은 최대의 정수를 출력
print(K*N**2)