from collections import defaultdict
import sys

# DNA의 수 N, 문자열의 길이 M
N, M = map(int, sys.stdin.readline().split())
# DNA를 담은 배열 DNA
DNA = [sys.stdin.readline().rstrip() for _ in range(N)]
# Hamming Distance의 합이 가장 작은 DNA answer, 그 Hamming Distance의 합 cnt
answer, cnt = '', 0

for i in range(M):
    alpha = defaultdict(int)

    for j in range(N):
        alpha[DNA[j][i]] += 1
    lst = sorted(list(alpha.items()), key=lambda x: (-x[1], x[0]))
    answer += lst[0][0]
    cnt += N - lst[0][1]
# answer와 cnt 출력
print(answer)
print(cnt)