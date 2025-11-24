import sys

# 점수의 개수 N, 제외되는 점수의 개수 K
N, K = map(int, sys.stdin.readline().split())
# 점수를 저장하는 배열 scores
scores = list(sorted(float(sys.stdin.readline()) for _ in range(N)))

# 절사 평균(N, K)
print('{:.2f}'.format(sum(scores[K:N-K])/(N-2*K)+1e-8))
# 보정 평균(N, K)
print('{:.2f}'.format((sum(scores[K:N-K])+scores[K]*K+scores[N-K-1]*K)/N+1e-8))