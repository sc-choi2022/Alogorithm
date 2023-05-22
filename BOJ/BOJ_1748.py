import sys

# 주어지는 수 N
N = int(sys.stdin.readline())
# 수의 자리수 L
L = len(str(N))
# 새로운 수의 자리수 answer
answer = 0

# L자리수를 가진 수의 개수와 L를 answer에 더한다.
answer += (N-10**(L-1)+1) * L
# L보다 작은 자리수의 수의 개수는 일정한 규칙으로 answer에 더해준다.
for i in range(L-1, 0, -1):
    answer += ((10**i-1)-10**(i-1)+1)*i
# 새로운 수의 자릿수를 출력
print(answer)