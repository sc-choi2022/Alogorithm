import sys

# 암호 P, 좋지 않은 기준 수 K
P, K = map(int, sys.stdin.readline().split())
# 소수 여부를 저장하는 배열 numbers
numbers = [0] * (K + 1)

for i in range(2, K+1):
    if not numbers[i]:
        for j in range(2*i, K+1, i):
            numbers[j] = 1
# K이하의 소수들로 조건을 확인하고 출력
for k in range(2, K):
    if numbers[k]:
        continue
    if not P % k:
        print('BAD', k)
        break
else:
    print('GOOD')