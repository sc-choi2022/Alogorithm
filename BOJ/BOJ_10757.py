import sys

# 두 수 A, B와 각 길이 lenA, lenB
A, B = map(list, sys.stdin.readline().rstrip().split())
lenA, lenB = len(A), len(B)
# A, B의 길이를 확인하여 길이를 맞춰준다.
if lenA > lenB:
    B = ['0']*(lenA - lenB) + B
else:
    A = ['0'] * (lenB - lenA) + A
# 정답 answer를 0으로 초기화
answer = 0
# A의 길이 만큼 진행 각 자리에서 계산 후 10의 제곱을 고려하여 answer에 더해준다.
for i in range(len(A)):
    answer += (int(A[-i-1]) + int(B[-i-1]))*10**i

# answer 출력
print(answer)